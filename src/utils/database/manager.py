from pydantic import BaseModel

from .url import UrlUtils, UrlConfig
from .engine import EngineUtils, EngineConfig
from .metadata import MetaDataUtils
from .sessionmaker import SessionMakerUtils, SessionMakerConfig


class DatabaseConfig(BaseModel):
    url: str
    pool_size: int
    max_overflow: int
    pool_timeout: int
    pool_pre_ping: bool


class DatabaseManager:
    def __init__(self, config: DatabaseConfig):
        self.url_utils = UrlUtils(
            UrlConfig(
                url=config.url,
            )
        )
        self.engine_utils = EngineUtils(
            EngineConfig(
                url=self.url,
                pool_size=config.pool_size,
                pool_timeout=config.pool_timeout,
                max_overflow=config.max_overflow,
                pool_pre_ping=config.pool_pre_ping
            )
        )
        self.metadata_utils = MetaDataUtils()
        self.sessionmaker_utils = SessionMakerUtils(
            SessionMakerConfig(
                engine=self.engine
            )
        )

    async def prepare(self) -> None:
        await self.metadata_utils.sync(self.engine)

    @property
    def engine(self):
        return self.engine_utils.engine
    
    @property
    def metadata(self):
        return self.metadata_utils.metadata
    
    @property
    def sessionmaker(self):
        return self.sessionmaker_utils.sessionmaker
    
    @property
    def url(self):
        return self.url_utils.url
    