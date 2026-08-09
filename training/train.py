from tensorflow.keras.preprocessing.image import ImageDataGenerator
from training.cnn_model import build_model

IMG_SIZE = 48
BATCH_SIZE = 32

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=10,
    zoom_range=0.1,
    horizontal_flip=True,
    validation_split=0.2
)

train_data = train_datagen.flow_from_directory(
    "dataset/train",
    target_size=(IMG_SIZE, IMG_SIZE),
    color_mode="grayscale",
    batch_size=BATCH_SIZE,
    class_mode="sparse",
    subset="training"
)

val_data = train_datagen.flow_from_directory(
    "dataset/train",
    target_size=(IMG_SIZE, IMG_SIZE),
    color_mode="grayscale",
    batch_size=BATCH_SIZE,
    class_mode="sparse",
    subset="validation"
)

model = build_model()

model.fit(train_data, validation_data=val_data, epochs=10)

model.save("models/emotion_model.keras")
print("Real model trained successfully")