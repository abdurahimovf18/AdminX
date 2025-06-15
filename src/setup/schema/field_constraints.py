from uuid import UUID
from typing import Unpack, Optional
from sqlalchemy import Column, Table, UniqueConstraint, CheckConstraint

from .base import BaseSchema, SchemaDict, SchemaParams


class FieldConstraintsSchemaDict(SchemaDict):
    field_id: UUID
    gte: Optional[float]
    gt: Optional[float]
    lt: Optional[float]
    lte: Optional[float]
    regex: Optional[str]
    min_length: Optional[int]
    max_length: Optional[int]
    unallowed_characters: Optional[str]
    allowed_characters: Optional[str]
    choices: Optional[list[str]]


class FieldConstraintsSchemaParams(SchemaParams):
    column: Column
    field_id: UUID
    table: Table


class FieldConstraintsSchema(BaseSchema):
    def __init__(self, **config: Unpack[FieldConstraintsSchemaParams]):
        super().__init__(**config)
        self.column: Column = config["column"]
        self.table: Table = config["table"]
        self.__field_id: UUID = config["field_id"]

        self.field_id: UUID
        self.gte: Optional[float] = config.get("gte")
        self.gt: Optional[float]
        self.lt: Optional[float]
        self.lte: Optional[float]
        self.regex: Optional[str]
        self.min_length: Optional[int]
        self.max_length: Optional[int]
        self.unallowed_characters: Optional[str]
        self.allowed_characters: Optional[str]
        self.choices: Optional[list[str]]

    @property
    def field_id(self) -> UUID:
        return self.__field_id
    
    @property
    def gte(self) -> Optional[float]:
        return None
        # for constraint in self.table.constraints:
        #     if constraint.

    @property
    def gt(self) -> Optional[float]:
        return None
    
    @property
    def lte(self) -> Optional[float]:
        return None
    
    @property
    def lt(self) -> Optional[float]:
        return None
    
    @property
    def regex(self) -> Optional[float]:
        return None
    
    @property
    def min_length(self) -> Optional[int]:
        return None
    
    @property
    def max_length(self) -> Optional[int]:
        return None
    
    @property
    def unallowed_characters(self) -> Optional[str]:
        return None
    
    @property
    def allowed_characters(self) -> Optional[str]:
        return None
    
    @property
    def choices(self) -> Optional[list[str]]:
        return None

    async def to_dict(self) -> FieldConstraintsSchemaDict:
        parent_data = await super().to_dict()

        data: FieldConstraintsSchemaDict = parent_data | {}
        data["gte"] = self.gte
        data["lte"] = self.lte
        data["lt"] = self.lt
        data["gt"] = self.gt
        data["regex"] = self.regex
        data["min_length"] = self.min_length
        data["max_length"] = self.max_length
        data["unallowed_characters"] = self.unallowed_characters
        data["allowed_characters"] = self.allowed_characters
        data["choices"] = self.choices

        return data