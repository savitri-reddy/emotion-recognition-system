from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from PIL import Image
from typing import List

from app.services.predictor import predict_emotion
from app.database.database import get_db
from app.database.crud import create_prediction, get_predictions
from app.api.schemas import PredictionResponse

router = APIRouter()


@router.post("/predict")
async def predict(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    image = Image.open(file.file)

    result = predict_emotion(image)

    create_prediction(
        db=db,
        image_name=file.filename,
        emotion=result["emotion"],
        confidence=result["confidence"]
    )

    return result


@router.get(
    "/predictions",
    response_model=List[PredictionResponse]
)
def prediction_history(
    db: Session = Depends(get_db)
):
    return get_predictions(db)