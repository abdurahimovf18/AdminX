import logging
from typing import Iterable
from src.setup.db.connection import DatabaseConnection


logger = logging.getLogger(__name__)


async def sync_models(connection: DatabaseConnection) -> None:
    async with connection.engine.begin() as conn:
        await conn.run_sync(connection.metadata.drop_all)
        await conn.run_sync(connection.metadata.create_all)


async def setup_database_connections(connections: Iterable["DatabaseConnection"]) -> None:
    """
    Initializes all provided database connections.

    Each connection object must implement an `async setup()` method and expose `.engine.url` for identification.

    Parameters:
    - connections: An iterable of DatabaseConnection instances to initialize.
    """
    logger.debug("Starting setup of database connections.")

    for connection in connections:
        db_url = getattr(connection.engine, 'url', '<unknown>')
        try:
            await connection.setup()
            logger.debug(f"Successfully set up Database at url: {db_url}")
        except Exception as exc:
            logger.warning(
                f"Failed to set up Database at url: {db_url}. Exception: {exc.__class__.__name__}: {exc}"
            )

    logger.info("Database setup process completed.")
