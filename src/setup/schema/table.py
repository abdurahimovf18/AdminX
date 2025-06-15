from uuid import UUID
from typing import Unpack
from .base import BaseSchema, SchemaDict, SchemaParams
from sqlalchemy import Table


class TableSchemaParmas(SchemaParams):
    table: Table
    database_id: UUID


class TableSchemaDict(SchemaDict):
    name: str
    database_id: UUID

 
class TableSchema(BaseSchema):    
    def __init__(self, **config: Unpack[TableSchemaParmas]):
        super().__init__(**config)
        self.table = config["table"]
        self.__database_id = config["database_id"]

    @property
    def database_id(self) -> UUID:
        return self.__database_id
    
    @property
    def name(self) -> str:
        return self.table.name

    async def to_dict(self) -> TableSchemaDict:
        parent_data = await super().to_dict()

        data = {
            "name": self.name,
            "database_id": self.database_id
        }

        return parent_data | data
