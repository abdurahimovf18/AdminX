from typing import Optional, Literal
from pydantic import BaseModel


class File(BaseModel):
   enable: Optional[bool] = None
   max_size: Optional[int] = None
   backups: Optional[int] = None


class Console(BaseModel):
   enable: Optional[bool] = None


class Logging(BaseModel):
    level: Optional[Literal["debug", "info", "warning", "error", "critical"]] = None
    format: Optional[Literal["json", "text"]] = None

    file: Optional[File] = None
    console: Optional[Console] = None
