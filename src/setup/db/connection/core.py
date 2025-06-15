from pydantic import BaseModel

from .fields.url import ConnectionUrl
from .fields.engine import ConnectionEngine
from .fields.metadata import ConnectionMetaData 
from .fields.sessionmaker import ConnectionSessionmaker


class ConnectionConfig(BaseModel):
    url: str
    pool_size: int
    max_overflow: int
    pool_timeout: int
    pool_pre_ping: bool


class DatabaseConnection:
    def __init__(self, config: ConnectionConfig):
        self.url_info = ConnectionUrl(
            url=config.url
        )
        self.engine_info = ConnectionEngine(
            url=self.url,
            pool_size=config.pool_size,
            pool_timeout=config.pool_timeout,
            max_overflow=config.max_overflow,
            pool_pre_ping=config.pool_pre_ping
        )
        self.metadata_info = ConnectionMetaData()
        self.sessionmaker_info = ConnectionSessionmaker(
            engine=self.engine
        )

    async def setup(self) -> None:
        await self.metadata_info.sync(self.engine)

    @property
    def engine(self):
        return self.engine_info.engine
    
    @property
    def metadata(self):
        return self.metadata_info.metadata
    
    @property
    def sessionmaker(self):
        return self.sessionmaker_info.sessionmaker
    
    @property
    def url(self):
        return self.url_info.url
    
    def __repr__(self):
        return f"{type(self).__name__}(url={self.url_info.make_url!s})"
    