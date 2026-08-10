from PIL import Image

from app.services.predictor import predict_emotion


def test_predict_emotion():

    image = Image.new(
        "L",
        (48, 48),
        color=128
    )

    result = predict_emotion(image)

    assert "emotion" in result
    assert "confidence" in result

    assert result["emotion"] in [
        "angry",
        "disgust",
        "fear",
        "happy",
        "neutral",
        "sad",
        "surprise"
    ]

    assert 0 <= result["confidence"] <= 1