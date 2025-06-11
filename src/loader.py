from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging

from src.config.logging_config import LOGGING_CONFIG

from src.config import databases_config

# Setup logging
logging.config.dictConfig(LOGGING_CONFIG)


@asynccontextmanager
async def lifespan(app: FastAPI):

    yield
