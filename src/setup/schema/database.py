from typing import Unpack
from .base import BaseSchema, SchemaDict, SchemaParams

from src.setup.db.connection import DatabaseConnection


class DatabaseSchemaDict(SchemaDict):
    name: str
    type: str
    connection_url: str
    is_internal: bool


class DatabaseSchemaParams(SchemaParams):
    connection: DatabaseConnection
    is_internal: bool


class DatabaseSchema(BaseSchema):

    def __init__(self, **config: Unpack[DatabaseSchemaParams]):
        super().__init__(**config)
        self.connection = config["connection"]
        self.__is_internal = config["is_internal"]

    @property
    def name(self) -> str:
        db_name = self.connection.engine.url.database or "unknown_database"
        return db_name
    
    @property
    def type(self) -> str:
        return self.connection.engine.url.drivername.split("+")[0]
    
    @property
    def connection_url(self) -> str:
        return str(self.connection.engine.url)
    
    @property
    def is_internal(self) -> bool:
        return self.__is_internal

    async def to_dict(self) -> DatabaseSchemaDict:
        parent_data = await super().to_dict()

        data = {
            "name": self.name,
            "type": self.type,
            "connection_url": self.connection_url,
            "is_internal": self.is_internal
        }

        return parent_data | data
