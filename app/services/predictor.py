import numpy as np
from PIL import Image

from app.services.inference import load_emotion_model
from app.config import CLASS_NAMES


def predict_emotion(image):

    model = load_emotion_model()


    image = image.resize((48,48))

    image = np.array(image)

    image = image / 255.0

    image = np.expand_dims(image,axis=0)


    prediction = model.predict(image)


    index = np.argmax(prediction)

    emotion = CLASS_NAMES[index]


    confidence = float(
        np.max(prediction)
    )


    return {
        "emotion": emotion,
        "confidence": confidence
    }