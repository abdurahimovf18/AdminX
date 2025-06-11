from .base_config import base_config
from .yml_schema.schema_fields.docs import Docs

from src.utils.misc import if_none


config = if_none(base_config.docs, Docs())

SWAGGER_URL = if_none(config.swagger_url, "/swagger")
REDOC_URL = if_none(config.redoc_url, "/redoc")
OPENAPI_URL = if_none(config.openapi_url, "/openapi.json")

APP_DEBUG = False
APP_TITLE = "AdminX: Dynamic Admin Panel API"
APP_DESCRIPTION = (
    "AdminX is a dynamic FastAPI-based admin panel that introspects external databases, "
    "generates full-featured CRUD APIs, and serves structured schema metadata for frontend rendering. "
    "It supports multiple databases, internal auth, and external integrations like RabbitMQ."
)
APP_VERSION = "1.0.0-beta"
