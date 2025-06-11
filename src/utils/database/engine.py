from pydantic import BaseModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine


class EngineConfig(BaseModel, total=False):
    url: str
    pool_size: int
    pool_timeout: int
    max_overflow: int
    pool_pre_ping: bool


class EngineUtils:
    def __init__(self, engine_config: EngineConfig):
        self.__engine = create_async_engine(**engine_config)

    @property
    def engine(self) -> AsyncEngine:
        return self.__engine
    