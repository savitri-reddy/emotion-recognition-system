from fastapi import FastAPI
from app.middleware.logger import logger

from fastapi import FastAPI

from app.api.routes import router
from app.database.database import Base, engine
from app.middleware.exception_handler import global_exception_handler

import app.database.models


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Emotion Recognition API",
    description="Emotion Recognition System using Deep Learning",
    version="1.0.0"
)


app.add_exception_handler(
    Exception,
    global_exception_handler
)

app.include_router(router)