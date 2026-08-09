from fastapi import FastAPI, UploadFile, File
from app.predictor import predict_emotion

app = FastAPI(title='Emotion Recognition API')

@app.get('/')
def home():
    return {'message': 'Emotion Recognition API Running'}

@app.post('/predict')
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()

    emotion, confidence = predict_emotion(image_bytes)

    return {
        'emotion': emotion,
        'confidence': round(confidence, 4)
    }