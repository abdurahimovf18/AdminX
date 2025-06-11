from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData

from src.config.db_config import DATABASE_DRIVERNAME_MAP
from src.config.yml_schema.db import DatabaseEntry

from .url import DatabaseUrlManager


class DatabaseManager:
    def __init__(self, config: DatabaseEntry):
        self.config = config

        self.url_manager: DatabaseUrlManager = DatabaseUrlManager(
            initial_url=self.config.url,
            url_env=self.config.url_env,
            database_drivername_map=DATABASE_DRIVERNAME_MAP
        )

        self._engine: AsyncEngine = create_async_engine(self.url_manager.url)
        self._sessionmaker: sessionmaker[AsyncSession] = sessionmaker(self.engine, class_=AsyncSession)
        self._metadata: MetaData = MetaData()

    async def sync(self) -> None:
        await self.bind_metadata()

    async def bind_metadata(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(self.metadata.reflect)

    @property
    def engine(self) -> AsyncEngine:
        return self._engine
    
    @property
    def sessionmaker(self) -> sessionmaker[AsyncSession]:
        return self._sessionmaker

    @property
    def metadata(self) -> MetaData:
        return self._metadata
    