"""
Naqal Skin AI - Model Training Script
Custom CNN trained on 92K faces (32K brown skin)
"""

import os
import json
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

# Paths
DATA_DIR = os.path.join(os.path.dirname(__file__), 'processed_data')
MODEL_DIR = os.path.join(os.path.dirname(__file__), 'ml', 'models')
os.makedirs(MODEL_DIR, exist_ok=True)

def load_data(limit=None):
    """Load training data from processed folder"""
    json_path = os.path.join(DATA_DIR, 'naqal_training_data.json')
    
    with open(json_path, 'r') as f:
        metadata = json.load(f)
    
    if limit:
        metadata = metadata[:limit]
    
    images = []
    labels = []
    
    print(f"Loading {len(metadata)} images...")
    
    for i, item in enumerate(metadata):
        img_path = os.path.join(DATA_DIR, item['image_path'])
        
        if os.path.exists(img_path):
            try:
                img = Image.open(img_path).resize((224, 224))
                img_array = np.array(img) / 255.0
                images.append(img_array)
                
                # Labels: [age, gender, acne, dark_circles, wrinkles, stains]
                labels.append([
                    item.get('age', 25) / 100.0,
                    1 if item.get('gender') == 'Female' else 0,
                    item.get('acne', 0),
                    item.get('dark_circles', 0),
                    item.get('wrinkles', 0),
                    item.get('stains', 0)
                ])
            except:
                continue
        
        if (i+1) % 10000 == 0:
            print(f"  Loaded {i+1}/{len(metadata)}")
    
    return np.array(images), np.array(labels)

def create_model():
    """Create Naqal Skin AI model"""
    
    # Base model - MobileNetV2 (pre-trained on ImageNet)
    base_model = tf.keras.applications.MobileNetV2(
        input_shape=(224, 224, 3),
        include_top=False,
        weights='imagenet'
    )
    base_model.trainable = False  # Freeze base
    
    model = models.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(6, activation='sigmoid')  # 6 outputs
    ])
    
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss='mse',
        metrics=['mae']
    )
    
    return model

def train():
    print("=" * 50)
    print("NAQAL SKIN AI - MODEL TRAINING")
    print("=" * 50)
    
    # Load data (start with 20K for speed)
    X, y = load_data(limit=5000)
    
    print(f"Data shape: {X.shape}")
    print(f"Labels shape: {y.shape}")
    
    # Split
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"Train: {len(X_train)}, Validation: {len(X_val)}")
    
    # Create model
    model = create_model()
    model.summary()
    
    # Callbacks
    checkpoint = ModelCheckpoint(
        os.path.join(MODEL_DIR, 'naqal_skin_ai.h5'),
        monitor='val_loss',
        save_best_only=True,
        mode='min'
    )
    
    early_stop = EarlyStopping(
        monitor='val_loss',
        patience=5,
        restore_best_weights=True
    )
    
    # Train
    print("\nTraining...")
    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=20,
        batch_size=32,
        callbacks=[checkpoint, early_stop],
        verbose=1
    )
    
    # Save final model
    model.save(os.path.join(MODEL_DIR, 'naqal_skin_ai_final.h5'))
    
    print("\n" + "=" * 50)
    print("TRAINING COMPLETE")
    print(f"Model saved to: {MODEL_DIR}")
    print("=" * 50)
    
    return history

if __name__ == "__main__":
    train()