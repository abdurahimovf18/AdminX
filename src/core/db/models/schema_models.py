import uuid

from sqlalchemy import (
    Table, Column, String, Boolean, UUID, ForeignKey,
    Float, Integer, JSON
)

from src.core.db.setup import SCHEMA_DATABASE_CONNECTION


metadata = SCHEMA_DATABASE_CONNECTION.metadata


def id_col():
    return Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


# --- Databases table ---
databases = Table(
    "databases", metadata,
    id_col(),
    Column("name", String, nullable=False),
    Column("type", String, nullable=False),
    Column("connection_url", String, nullable=False),
    Column("is_internal", Boolean, nullable=False),
)

# --- Tables table ---
tables = Table(
    "tables", metadata,
    id_col(),
    Column("database_id", UUID(as_uuid=True), ForeignKey("databases.id", ondelete="RESTRICT"), nullable=False),
    Column("name", String, nullable=False),
)

# --- Fields table ---
fields = Table(
    "fields", metadata,
    id_col(),
    Column("table_id", UUID(as_uuid=True), ForeignKey("tables.id", ondelete="RESTRICT"), nullable=False),
    Column("name", String, nullable=False),
    Column("type", String, nullable=False),
)

# --- FieldWidget table ---
field_widget = Table(
    "field_widget", metadata,
    id_col(),
    Column("field_id", UUID(as_uuid=True), ForeignKey("fields.id", ondelete="RESTRICT"), nullable=False),
    Column("example", String, nullable=True),
    Column("description", String, nullable=True),
    Column("hidden", Boolean, nullable=True),
    Column("required", Boolean, nullable=False, default=True),
    Column("primary_key", Boolean, nullable=False)
)

# --- FieldConstraints table ---
field_constraints = Table(
    "field_constraints", metadata,
    id_col(),
    Column("field_id", UUID(as_uuid=True), ForeignKey("fields.id", ondelete="RESTRICT"), nullable=False),
    Column("gte", Float, nullable=True),
    Column("gt", Float, nullable=True),
    Column("lt", Float, nullable=True),
    Column("lte", Float, nullable=True),
    Column("regex", String, nullable=True),
    Column("min_length", Integer, nullable=True),
    Column("max_length", Integer, nullable=True),
    Column("unallowed_characters", String, nullable=True),
    Column("allowed_characters", String, nullable=True),
    Column("choices", JSON, nullable=True),
)
