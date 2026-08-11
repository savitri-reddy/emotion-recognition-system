import logging
import os

# Create logs directory if it does not exist
os.makedirs("logs", exist_ok=True)

# Main application logger
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Separate prediction logger
prediction_logger = logging.getLogger("prediction_logger")
prediction_logger.setLevel(logging.INFO)

if not prediction_logger.handlers:
    handler = logging.FileHandler("logs/prediction.log")
    handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )
    prediction_logger.addHandler(handler)