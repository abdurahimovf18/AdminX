from .base_config import base_config, ROOT
from .yml_schema.schema_fields.logging import Logging, File, Console
from src.utils.misc import if_none


FORMAT_MAP = {
    "json": "json",
    "text": "text"
}

# Load base logging config
config = if_none(base_config.logging, Logging())

# General logging settings
LOG_LEVEL = if_none(config.level, "info")
FORMAT_TYPE = if_none(config.format, "text")
FORMAT = FORMAT_MAP[FORMAT_TYPE]

# File logging settings
file_config = if_none(config.file, File())
LOG_TO_FILE = if_none(file_config.enable, True)
MAX_SIZE = if_none(file_config.max_size, 10) * 1024 * 1024
BACKUPS = if_none(file_config.backups, 3)
LOG_FILENAME = ROOT / "logs/adminx.log"

LOG_FILENAME.parent.mkdir(exist_ok=True, parents=True)

# Console logging settings
console_config = if_none(config.console, Console())
LOG_TO_CONSOLE = if_none(console_config.enable, False)


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "text": {
            "format": "[{asctime}] [{levelname:<8}] [{name}] {message}",
            "style": "{",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(levelname)s %(name)s %(message)s",
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": FORMAT_TYPE,
            "level": "DEBUG",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": FORMAT_TYPE,
            "filename": LOG_FILENAME,
            "maxBytes": MAX_SIZE,
            "backupCount": BACKUPS,
            "level": "INFO",
            "encoding": "utf-8",
        }
    },

    "root": {
        "handlers": [],
        "level": LOG_LEVEL.upper(),
    },

    "loggers": {
        "adminx": {
            "handlers": [],
            "level": LOG_LEVEL.upper(),
            "propagate": False,
        },
    },
}

# Dynamically assign handlers based on config
if LOG_TO_CONSOLE:
    LOGGING_CONFIG["root"]["handlers"].append("console")
    LOGGING_CONFIG["loggers"]["adminx"]["handlers"].append("console")

if LOG_TO_FILE:
    LOGGING_CONFIG["root"]["handlers"].append("file")
    LOGGING_CONFIG["loggers"]["adminx"]["handlers"].append("file")
