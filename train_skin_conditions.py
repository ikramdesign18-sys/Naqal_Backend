"""
Naqal Skin AI v3 - Train on Labeled Skin Conditions
Cambridge Skin Analysis dataset with severity labels
"""

import pandas as pd
import numpy as np
import os
from PIL import Image
import tensorflow as tf
from tensorflow.keras import layers, models, callbacks

# ============================================
# CONFIGURATION
# ============================================
DATASET_PATH = 'datasets/skin_type_classification_dataset'
EXCEL_FILE = os.path.join(DATASET_PATH, 'skinalaysis_labeling_train1.xlsx')
VALID_EXCEL = os.path.join(DATASET_PATH, 'skinanalysis_valid1.xlsx')
IMAGE_FOLDER = os.path.join(DATASET_PATH, 'train')
MODEL_SAVE_PATH = 'ml/models/naqal_skin_ai_v3.keras'

print("=" * 50)
print("NAQAL SKIN AI v3 - SKIN CONDITION TRAINING")
print("=" * 50)

# Load labels
df_train = pd.read_excel(EXCEL_FILE)
df_valid = pd.read_excel(VALID_EXCEL)
print(f"Train labels: {len(df_train)}, Valid labels: {len(df_valid)}")

# ============================================
# BUILD FILE INDEX
# ============================================
print("\nBuilding file index...")
all_files = {}
for skin_type in ['oily', 'dry', 'normal', 'combination']:
    type_folder = os.path.join(IMAGE_FOLDER, skin_type)
    if os.path.exists(type_folder):
        for f in os.listdir(type_folder):
            if f.endswith(('.jpg', '.jpeg', '.png')):
                base = f.split('.rf.')[0] if '.rf.' in f else f.rsplit('.', 1)[0]
                all_files[base] = os.path.join(type_folder, f)
print(f"Found {len(all_files)} image files")

# ============================================
# MAP LABELS
# ============================================
def map_labels(df):
    labels = []
    for _, row in df.iterrows():
        labels.append([
            float(row['Acne_Severity (0-5)']) / 5.0,
            float(row['Redness Severity (0-5)']) / 5.0,
            float(row['Dark circles around eyes(0-5)']) / 5.0,
            float(row['Open pores (0-5)']) / 5.0,
            1.0 - (float(row['Dehydration (0-5)(5 very dehydrated)']) / 5.0),
            float(row['Skin sensitivity (0-5)']) / 5.0,
        ])
    return np.array(labels, dtype=np.float32)

# ============================================
# LOAD IMAGES AND LABELS TOGETHER
# ============================================
def load_dataset(df):
    images = []
    labels = []
    
    for _, row in df.iterrows():
        image_id = str(row['Image_ID'])
        base_id = image_id.split('.rf.')[0] if '.rf.' in image_id else image_id.rsplit('.', 1)[0]
        
        found = False
        for key, path in all_files.items():
            if base_id in key or key in base_id:
                try:
                    img = Image.open(path).convert('RGB').resize((224, 224))
                    images.append(np.array(img, dtype=np.float32) / 255.0)
                    labels.append([
                        float(row['Acne_Severity (0-5)']) / 5.0,
                        float(row['Redness Severity (0-5)']) / 5.0,
                        float(row['Dark circles around eyes(0-5)']) / 5.0,
                        float(row['Open pores (0-5)']) / 5.0,
                        1.0 - (float(row['Dehydration (0-5)(5 very dehydrated)']) / 5.0),
                        float(row['Skin sensitivity (0-5)']) / 5.0,
                    ])
                    found = True
                    break
                except:
                    continue
    
    return np.array(images, dtype=np.float32), np.array(labels, dtype=np.float32)

print("\nLoading training data...")
X_train, y_train = load_dataset(df_train)
print(f"Train: {X_train.shape}, Labels: {y_train.shape}")

print("Loading validation data...")
X_valid, y_valid = load_dataset(df_valid)
print(f"Valid: {X_valid.shape}, Labels: {y_valid.shape}")

if len(X_train) == 0:
    print("\n❌ No images loaded! Check image folder and Excel IDs.")
    exit()

# ============================================
# BUILD MODEL
# ============================================
print("\nBuilding model...")
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)
base_model.trainable = False

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(6, activation='sigmoid')
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='mse',
    metrics=['mae']
)

model.summary()

# ============================================
# TRAIN
# ============================================
print("\n" + "=" * 50)
print("TRAINING NAQAL AI v3")
print("=" * 50)

early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
checkpoint = callbacks.ModelCheckpoint(MODEL_SAVE_PATH, monitor='val_loss', save_best_only=True)

history = model.fit(
    X_train, y_train,
    validation_data=(X_valid, y_valid),
    epochs=50,
    batch_size=8,
    callbacks=[early_stop, checkpoint],
    verbose=1
)

# ============================================
# SAVE
# ============================================
model.save(MODEL_SAVE_PATH)
print(f"\n✅ Model saved to: {MODEL_SAVE_PATH}")
print(f"Best validation loss: {min(history.history['val_loss']):.4f}")
print("\nNaqal AI v3 predicts ALL 6 skin metrics directly!")
print("=" * 50)