from typing import TypedDict
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine


class EngineConfig(TypedDict):
    url: str
    pool_size: int
    pool_timeout: int
    max_overflow: int
    pool_pre_ping: bool


class ConnectionEngine:
    def __init__(self, **config: EngineConfig):
        self.__engine = create_async_engine(**config)

    @property
    def engine(self) -> AsyncEngine:
        return self.__engine
    