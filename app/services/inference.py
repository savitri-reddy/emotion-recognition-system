from tensorflow.keras.models import load_model
from app.config import MODEL_PATH


model = None


def load_emotion_model():

    global model

    if model is None:
        model = load_model(MODEL_PATH)

    return model