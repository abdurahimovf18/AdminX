from uuid import UUID
from typing import Unpack
from sqlalchemy import Column

from .base import BaseSchema, SchemaDict, SchemaParams
from src.utils.database import get_json_type


class FieldWidgetSchemaDict(SchemaDict):
    field_id: UUID
    description: str
    example: str
    hidden: bool
    primary_key: bool
    required: bool


class FieldWidgetSchemaParams(SchemaParams):
    column: Column
    field_id: UUID
    table_id: UUID


class FieldWidgetSchema(BaseSchema):

    def __init__(self, **config: Unpack[FieldWidgetSchemaParams]):
        super().__init__(**config)
        self.__field_id: UUID = config["field_id"]
        self.column = config["column"]
        self.table_id = config["table_id"]

    @property
    def type(self):
        return get_json_type(self.column)

    @property
    def field_id(self) -> UUID:
        return self.__field_id
    
    @property
    def example(self) -> str:
        if self.type == "string":
            return self.type
        if self.type == "number":
            return "0"
        if self.type == "object":
            return "{}"
        if self.type == "array":
            return "[]"
        return "string"

    @property
    def description(self) -> str:
        text = "A "
        if self.required:
            text += "required "
        if self.primary_key:
            text += "primary key "
        
        text += f"column of the table at id: {self.table_id}"

        return text
    
    @property
    def primary_key(self) -> bool:
        return self.column.primary_key

    @property
    def hidden(self) -> bool:
        is_pk_col = self.column.primary_key
        is_any_default = self.column.default or self.column.server_default
        return bool(is_pk_col and is_any_default)

    @property
    def required(self) -> bool:
        return self.column.nullable or False

    async def to_dict(self) -> FieldWidgetSchemaDict:
        parent_data = await super().to_dict()

        data = {
            "field_id": self.field_id,
            "example": self.example,
            "description": self.description,
            "hidden": self.hidden,
            "primary_key": self.primary_key,
            "required": self.required
        }

        return parent_data | data
    