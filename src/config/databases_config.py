import os
from typing import TypedDict
from logging import getLogger

from .base_config import base_config
from .yml_schema.schema_fields.databases import (
    Databases,
    ConnectionSettings,
    DefaultSettings,
)
from src.utils.misc import if_none

logger = getLogger(__name__)

# Load top-level database configuration from base config
config = if_none(base_config.databases, Databases())

# Identify which configured connection is the system database
SYSTEM_DB_CONNECTION_NAME = config.system_db
if SYSTEM_DB_CONNECTION_NAME is None:
    logger.critical(
        "Missing configuration: 'databases.system_db' must be set in config.yml. "
        "It tells the app which connection is the system database."
    )
    raise ValueError("Missing required configuration: 'databases.system_db'")

# Load default pool settings to fall back on when connection-specific values are missing
default_settings = if_none(config.default_settings, DefaultSettings())
POOL_SIZE = if_none(default_settings.pool_size, 20)
MAX_OVERFLOW = if_none(default_settings.max_overflow, 30)
POOL_TIMEOUT = if_none(default_settings.pool_timeout, 30)
POOL_PRE_PING = if_none(default_settings.pool_pre_ping, True)

# Typed dictionary to represent a resolved connection
class ConnectionInfo(TypedDict):
    config_name: str
    url: str
    pool_size: int
    max_overflow: int
    pool_timeout: int
    pool_pre_ping: bool

# Load all declared database connections
CONFIG_CONNECTIONS: dict[str, ConnectionSettings] = if_none(config.connections, {})

# Final resolved connections and the designated system connection
CONNECTIONS: list[ConnectionInfo] = []
SYSTEM_CONNECTION: ConnectionInfo | None = None

for name, connection in CONFIG_CONNECTIONS.items():
    # Fetch actual database URL from environment using key from config
    connection_url = os.getenv(connection.env)

    if connection_url is None:
        logger.critical(
            f"Missing environment variable for 'databases.{name}.env': '{connection.env}' is not defined. "
            "You must set this environment variable (e.g., in your .env file or deployment secrets)."
        )
        raise KeyError(
            f"Environment variable '{connection.env}' required by 'databases.{name}.env' is not set."
        )

    new_connection_info: ConnectionInfo = {
        "config_name": name,
        "url": connection_url,
        "pool_size": if_none(connection.pool_size, POOL_SIZE),
        "max_overflow": if_none(connection.max_overflow, MAX_OVERFLOW),
        "pool_timeout": if_none(connection.pool_timeout, POOL_TIMEOUT),
        "pool_pre_ping": if_none(connection.pool_pre_ping, POOL_PRE_PING),
    }

    # Store as system connection or append to the others
    if name == SYSTEM_DB_CONNECTION_NAME:
        SYSTEM_CONNECTION = new_connection_info
    else:
        CONNECTIONS.append(new_connection_info)

# Ensure the system connection actually exists
if SYSTEM_CONNECTION is None:
    logger.critical(
        f"'databases.system_db' is set to '{SYSTEM_DB_CONNECTION_NAME}', "
        f"but no connection by that name is declared under 'databases.{SYSTEM_DB_CONNECTION_NAME}'."
    )
    raise KeyError(
        f"Missing connection definition for system DB: 'databases.{SYSTEM_DB_CONNECTION_NAME}'"
    )
