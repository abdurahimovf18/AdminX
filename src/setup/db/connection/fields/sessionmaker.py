from typing import TypedDict

from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker


class SessionmakerConfig(TypedDict):
    engine: AsyncEngine


class ConnectionSessionmaker:
    def __init__(self, **config: SessionmakerConfig):
        self.__sessionmaker: sessionmaker[AsyncSession] = sessionmaker(config["engine"], class_=AsyncSession)

    @property
    def sessionmaker(self) -> sessionmaker[AsyncSession]:
        return self.__sessionmaker
