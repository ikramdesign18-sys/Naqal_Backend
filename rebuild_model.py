import tensorflow as tf
from tensorflow.keras import layers, models

print("Rebuilding Naqal Ultimate in Keras 2 format...")

base = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)
base.trainable = False

model = models.Sequential([
    base,
    layers.GlobalAveragePooling2D(),
    layers.Dense(512, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(128, activation='relu'),
    layers.Dense(6, activation='sigmoid')
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])
model.save('ml/models/naqal_ultimate.h5')
print("Model saved")