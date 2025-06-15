from fastapi import FastAPI
from src.config import docs_config
from .loader import lifespan

from src.utils import database


app = FastAPI(
    debug = docs_config.APP_DEBUG,
    docs_url=docs_config.SWAGGER_URL,
    redoc_url=docs_config.REDOC_URL,
    title=docs_config.APP_TITLE,
    openapi_url=docs_config.OPENAPI_URL,
    description=docs_config.APP_DESCRIPTION,
    version=docs_config.APP_VERSION,
    lifespan=lifespan,
)
