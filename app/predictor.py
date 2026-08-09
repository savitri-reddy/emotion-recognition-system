import numpy as np
import cv2
import tensorflow as tf

model = tf.keras.models.load_model('models/emotion_model.keras')

EMOTIONS = ['Angry', 'Happy', 'Sad', 'Surprise', 'Neutral']

def predict_emotion(image_bytes):
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)

    img = cv2.resize(img, (48, 48))
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=(0, -1))

    prediction = model.predict(img)

    emotion = EMOTIONS[np.argmax(prediction)]
    confidence = float(np.max(prediction))

    return emotion, confidence