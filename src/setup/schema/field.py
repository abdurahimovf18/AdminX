from uuid import UUID
from typing import Unpack
from sqlalchemy import Column

from .base import BaseSchema, SchemaDict, SchemaParams
from src.utils.database import get_json_type


class FieldSchemaParams(SchemaParams):
    table_id: UUID
    column: Column


class FieldSchemaDict(SchemaDict):
    table_id: UUID
    type: str
    name: str


class FieldSchema(BaseSchema):

    def __init__(self, **config: Unpack[FieldSchemaParams]):
        super().__init__(**config)
        self.column: Column = self.config["column"]
        self.__table_id: UUID = self.config["table_id"]

    @property
    def name(self):
        return self.column.name
    
    @property
    def type(self) -> str:
        return get_json_type(self.column.type)

    @property
    def table_id(self) -> UUID:
        return self.__table_id

    async def to_dict(self) -> FieldSchemaDict:
        parent_data = await super().to_dict()
    
        data = {
            "table_id": self.table_id,
            "name": self.name,
            "type": self.type
        }

        return parent_data | data

