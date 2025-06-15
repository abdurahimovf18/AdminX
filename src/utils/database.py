from sqlalchemy import (
    Integer, Numeric, String, Boolean,
    Date, DateTime, Time, Interval,
    JSON, ARRAY, Uuid, LargeBinary, Column
)
from sqlalchemy.sql.sqltypes import _Binary, PickleType, TupleType, NullType, Variant
from sqlalchemy import types


sqlalchemy_type_vars = {
    name: typ for name, typ in vars(types).items()
    if isinstance(typ, type) and issubclass(typ, types.TypeEngine)
}


sqlalchemy_json_type_map = {
    Integer: "integer",
    Numeric: "number",
    String: "string",
    Boolean: "boolean",
    Date: "string",
    DateTime: "string",
    Time: "string",
    Interval: "string",
    JSON: "object",
    ARRAY: "array",
    Uuid: "string",
    _Binary: "string",
    PickleType: "object",
    TupleType: "array",
    Variant: "string", 
    NullType: "string",
    LargeBinary: "string"
}


def get_json_type(type_: Column | str) -> str:
    if isinstance(type_, str):
        type_ = sqlalchemy_type_vars.get(type_, String)()

    if isinstance(type_, Column):
        type_ = type_.type

    for base in type(type_).__mro__:
        if base in sqlalchemy_json_type_map:
            return sqlalchemy_json_type_map[base]

    return "string"
