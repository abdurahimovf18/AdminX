from uuid import UUID, uuid4
from typing import TypedDict, Unpack
from src.setup.db.connection import DatabaseConnection
import json


class SchemaDict(TypedDict):
    id: UUID

class SchemaParams(TypedDict):
    pass


class BaseSchema:
    def __init__(self, **config: Unpack[SchemaParams]):
        self.config = config
        self.__id: UUID = uuid4()
    
    @property
    def id(self) -> UUID:
        return self.__id

    async def to_dict(self) -> SchemaDict:
        return {
            "id": self.id
        }
    
    async def to_json(self) -> str:
        return json.dumps(await self.to_dict())

    def __repr__(self) -> str:
        params = ", ".join(f"{key}={val}" for key, val in self.config.items())
        return f"{type(self).__name__}({params})"
