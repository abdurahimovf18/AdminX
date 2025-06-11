from typing import Optional
from pydantic import BaseModel

from .schema_fields.databases import Databases
from .schema_fields.docs import Docs
from .schema_fields.logging import Logging
from .schema_fields.server import Server


class YmlConfigSchema(BaseModel):
    server: Optional[Server] = None
    databases: Optional[Databases] = None
    logging: Optional[Logging] = None
    docs: Optional[Docs] = None
