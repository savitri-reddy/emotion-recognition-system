from app.database.models import Prediction


def create_prediction(
    db,
    image_name,
    emotion,
    confidence
):

    prediction = Prediction(
        image_name=image_name,
        emotion=emotion,
        confidence=confidence
    )

    db.add(prediction)

    db.commit()

    db.refresh(prediction)

    return prediction


def get_predictions(db):

    return db.query(
        Prediction
    ).all()