from typing import Optional
from pydantic import BaseModel


class Server(BaseModel):
    workers: Optional[int] = None
    threads: Optional[int] = None
    timeout: Optional[int] = None
    keep_alive: Optional[int] = None
