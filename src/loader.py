from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging

from src.config.logging_config import LOGGING_CONFIG
from src.core.db.setup import DATABASE_CONNECTIONS_COLLECTION, SCHEMA_DATABASE_CONNECTION
from src.utils.setup import setup_database_connections

import src.core.db.models


# Setup logging
logging.config.dictConfig(LOGGING_CONFIG)


@asynccontextmanager
async def lifespan(app: FastAPI):

    await setup_database_connections(DATABASE_CONNECTIONS_COLLECTION)

    yield
