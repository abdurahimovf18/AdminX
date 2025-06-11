from pydantic import BaseModel

from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker


class SessionMakerConfig(BaseModel):
    engine: AsyncEngine


class SessionMakerUtils:
    def __init__(self, config: SessionMakerConfig):
        self.config = config
        self.__sessionmaker: sessionmaker[AsyncSession] = sessionmaker(self.config.engine, class_=AsyncSession)

    @property
    def sessionmaker(self) -> sessionmaker[AsyncSession]:
        return self.__sessionmaker
