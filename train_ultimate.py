"""
NAQAL AI ULTIMATE - Train on ALL datasets combined
9,942 labeled skin condition images + 86K faces
"""

import os
import json
import numpy as np
import pandas as pd
from PIL import Image
import tensorflow as tf
from tensorflow.keras import layers, models, callbacks
import cv2

# ============================================
# CONFIG
# ============================================
DATASETS = 'datasets'
CAMBRIDGE = os.path.join(DATASETS, 'skin_type_classification_dataset')
SKIN_PROBLEM = os.path.join(DATASETS, 'skin_problem_detection')
SKIN_ISSUES = os.path.join(DATASETS, 'GlowMix/Skin Issues Dataset/Skin v2')
MODEL_PATH = 'ml/models/naqal_ultimate.keras'

print("=" * 60)
print("NAQAL AI ULTIMATE TRAINING")
print("9,942 labeled images from 3 datasets")
print("=" * 60)

# ============================================
# DATASET 1: Cambridge (severity scores 0-5)
# ============================================
print("\n[1/3] Loading Cambridge dataset...")

df = pd.read_excel(os.path.join(CAMBRIDGE, 'skinalaysis_labeling_train1.xlsx'))
df2 = pd.read_excel(os.path.join(CAMBRIDGE, 'skinanalysis_valid1.xlsx'))
df_all = pd.concat([df, df2])

# Build file index
file_index = {}
for skin_type in ['oily', 'dry', 'normal', 'combination']:
    folder = os.path.join(CAMBRIDGE, 'train', skin_type)
    if os.path.exists(folder):
        for f in os.listdir(folder):
            if f.endswith(('.jpg', '.jpeg', '.png')):
                base = f.split('.rf.')[0] if '.rf.' in f else f.rsplit('.', 1)[0]
                file_index[base] = os.path.join(folder, f)

cambridge_images = []
cambridge_labels = []

for _, row in df_all.iterrows():
    image_id = str(row['Image_ID'])
    base_id = image_id.split('.rf.')[0] if '.rf.' in image_id else image_id.rsplit('.', 1)[0]
    
    for key, path in file_index.items():
        if base_id in key or key in base_id:
            try:
                img = Image.open(path).convert('RGB').resize((224, 224))
                cambridge_images.append(np.array(img, dtype=np.float32) / 255.0)
                cambridge_labels.append([
                    float(row['Acne_Severity (0-5)']) / 5.0,
                    float(row['Redness Severity (0-5)']) / 5.0,
                    float(row['Dark circles around eyes(0-5)']) / 5.0,
                    float(row['Open pores (0-5)']) / 5.0,
                    1.0 - (float(row['Dehydration (0-5)(5 very dehydrated)']) / 5.0),
                    float(row['Skin sensitivity (0-5)']) / 5.0,
                ])
                break
            except:
                continue

print(f"  Cambridge: {len(cambridge_images)} images")

# ============================================
# DATASET 2: Skin Problem Detection (YOLO labels → severity)
# ============================================
print("\n[2/3] Loading Skin Problem Detection dataset...")

# Class mapping
CLASS_TO_METRIC = {
    'Acne': 0, 'Blackheads': 0, 'Whiteheads': 0,  # → acne
    'Skin-Redness': 1,                              # → redness
    'Eyebags': 2, 'Dark-Spots': 2,                 # → dark circles
    'Englarged-Pores': 3,                          # → texture
    'Dry-Skin': 4, 'Oily-Skin': 4,                 # → hydration
    'Wrinkles': 3,                                 # → texture
}

skin_problem_images = []
skin_problem_labels = []

for split in ['train', 'valid']:
    img_dir = os.path.join(SKIN_PROBLEM, split, 'images')
    label_dir = os.path.join(SKIN_PROBLEM, split, 'labels')
    
    if not os.path.exists(img_dir):
        continue
    
    for img_file in os.listdir(img_dir):
        if not img_file.endswith(('.jpg', '.jpeg', '.png')):
            continue
        
        # Load image
        img_path = os.path.join(img_dir, img_file)
        try:
            img = Image.open(img_path).convert('RGB').resize((224, 224))
        except:
            continue
        
        # Load YOLO labels
        label_file = os.path.join(label_dir, img_file.rsplit('.', 1)[0] + '.txt')
        scores = [0.0, 0.0, 0.0, 0.0, 0.5, 0.0]  # Default: neutral hydration
        
        if os.path.exists(label_file):
            with open(label_file) as f:
                for line in f:
                    parts = line.strip().split()
                    if len(parts) >= 1:
                        class_id = int(parts[0])
                        # Map class to metric index
                        class_name = ['Acne','Blackheads','Dark-Spots','Dry-Skin','Englarged-Pores',
                                     'Eyebags','Oily-Skin','Skin-Redness','Whiteheads','Wrinkles'][class_id]
                        if class_name in CLASS_TO_METRIC:
                            metric_idx = CLASS_TO_METRIC[class_name]
                            scores[metric_idx] = max(scores[metric_idx], 0.6 + (scores[metric_idx] * 0.4))
        
        skin_problem_images.append(np.array(img, dtype=np.float32) / 255.0)
        skin_problem_labels.append(scores)

print(f"  Skin Problem: {len(skin_problem_images)} images")

# ============================================
# DATASET 3: Skin Issues (folder-based labels)
# ============================================
print("\n[3/3] Loading Skin Issues dataset...")

FOLDER_TO_METRIC = {
    'blackheades': 0,      # acne
    'dark spots': 2,       # dark circles
    'pores': 3,            # texture
    'wrinkles': 3,         # texture
}

issues_images = []
issues_labels = []

for folder in os.listdir(SKIN_ISSUES):
    if folder.startswith('.') or folder not in FOLDER_TO_METRIC:
        continue
    
    folder_path = os.path.join(SKIN_ISSUES, folder)
    metric_idx = FOLDER_TO_METRIC[folder]
    
    for f in os.listdir(folder_path):
        if not f.endswith(('.jpg', '.jpeg', '.png')):
            continue
        try:
            img = Image.open(os.path.join(folder_path, f)).convert('RGB').resize((224, 224))
            scores = [0.0] * 6
            scores[metric_idx] = 0.7
            if metric_idx == 3:  # texture base
                scores[3] = 0.5
            issues_images.append(np.array(img, dtype=np.float32) / 255.0)
            issues_labels.append(scores)
        except:
            continue

print(f"  Skin Issues: {len(issues_images)} images")

# ============================================
# COMBINE ALL DATA
# ============================================
print("\n" + "=" * 60)
print("COMBINING ALL DATASETS")

X = np.array(cambridge_images + skin_problem_images + issues_images, dtype=np.float32)
y = np.array(cambridge_labels + skin_problem_labels + issues_labels, dtype=np.float32)

print(f"Total training samples: {len(X)}")
print(f"Acne avg: {np.mean(y[:,0]):.2f}, Redness avg: {np.mean(y[:,1]):.2f}")
print(f"Dark circles avg: {np.mean(y[:,2]):.2f}, Texture avg: {np.mean(y[:,3]):.2f}")
print(f"Hydration avg: {np.mean(y[:,4]):.2f}, Sensitivity avg: {np.mean(y[:,5]):.2f}")

# ============================================
# TRAIN/VAL SPLIT
# ============================================
from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Train: {len(X_train)}, Val: {len(X_val)}")

# ============================================
# BUILD MODEL
# ============================================
print("\nBuilding Ultimate Naqal Model...")
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)
base_model.trainable = False

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(512, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(128, activation='relu'),
    layers.Dense(6, activation='sigmoid')
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0005), loss='mse', metrics=['mae'])
model.summary()

# ============================================
# TRAIN
# ============================================
print("\n" + "=" * 60)
print("TRAINING NAQAL ULTIMATE")
print("=" * 60)

early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=15, restore_best_weights=True)
reduce_lr = callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=5, min_lr=1e-6)
checkpoint = callbacks.ModelCheckpoint(MODEL_PATH, monitor='val_loss', save_best_only=True)

history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=100,
    batch_size=16,
    callbacks=[early_stop, reduce_lr, checkpoint],
    verbose=1
)

# ============================================
# SAVE
# ============================================
model.save(MODEL_PATH)
print(f"\n✅ Ultimate model saved: {MODEL_PATH}")
print(f"Best val_loss: {min(history.history['val_loss']):.4f}")
print(f"Samples: {len(X)}")
print("NAQAL AI ULTIMATE - READY")