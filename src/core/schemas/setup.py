from src.setup.db.connection import DatabaseConnection
from src.core.db.setup import SCHEMA_DATABASE_CONNECTION, DATABASE_CONNECTIONS_COLLECTION

from src.setup.schema.database import DatabaseSchema
from src.setup.schema.field import FieldSchema
from src.setup.schema.field_widget import FieldWidgetSchema
from src.setup.schema.field_constraints import FieldConstraintsSchema

from src.utils.setup import sync_models


async def setup_database_table(connection: DatabaseConnection):
    pass


async def setup_schema_database():
    await sync_models(SCHEMA_DATABASE_CONNECTION)

    await setup_database_table()

