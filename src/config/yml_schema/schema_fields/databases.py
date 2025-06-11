from typing import Optional
from pydantic import BaseModel


class DefaultSettings(BaseModel):
    pool_size: Optional[int] = None
    max_overflow: Optional[int] = None
    pool_timeout: Optional[int] = None
    pool_pre_ping: Optional[bool] = None


class ConnectionSettings(DefaultSettings):
    env: str


class Databases(BaseModel):
    system_db: Optional[str] = None
    default_settings: Optional[DefaultSettings] = None
    connections: Optional[dict[str, ConnectionSettings]] = None
