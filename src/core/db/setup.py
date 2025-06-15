from src.config.databases_config import CONNECTIONS, CONFIG_SYSTEM_CONNECTION, CONFIG_SCHEMA_DATABASE

from src.setup.db.connection import DatabaseConnection, ConnectionConfig


SCHEMA_DATABASE_CONNECTION = DatabaseConnection(
    ConnectionConfig(
        url=CONFIG_SCHEMA_DATABASE["url"],
        pool_size=CONFIG_SCHEMA_DATABASE["pool_size"],
        max_overflow=CONFIG_SCHEMA_DATABASE["max_overflow"],
        pool_timeout=CONFIG_SCHEMA_DATABASE["pool_timeout"],
        pool_pre_ping=CONFIG_SCHEMA_DATABASE["pool_pre_ping"]
    )
)


SYSTEM_DATABASE_CONNECTION = DatabaseConnection(
    ConnectionConfig(
        url=CONFIG_SYSTEM_CONNECTION["url"],
        pool_size=CONFIG_SYSTEM_CONNECTION["pool_size"],
        max_overflow=CONFIG_SYSTEM_CONNECTION["max_overflow"],
        pool_timeout=CONFIG_SYSTEM_CONNECTION["pool_timeout"],
        pool_pre_ping=CONFIG_SYSTEM_CONNECTION["pool_pre_ping"]
    )
)

DATABASE_CONNECTION_MAP: dict[str, DatabaseConnection] = dict()


for connection_config in CONNECTIONS:
    DATABASE_CONNECTION_MAP[connection_config["config_name"]] = DatabaseConnection(
        ConnectionConfig(
            url=connection_config["url"],
            pool_size=connection_config["pool_size"],
            max_overflow=connection_config["max_overflow"],
            pool_timeout=connection_config["pool_timeout"],
            pool_pre_ping=connection_config["pool_pre_ping"]
        )
    )


DATABASE_CONNECTIONS_COLLECTION: set[DatabaseConnection] = set(
    (
        *DATABASE_CONNECTION_MAP.values(), 
        SYSTEM_DATABASE_CONNECTION,
        SCHEMA_DATABASE_CONNECTION,
    )
)
