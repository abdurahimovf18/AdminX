from typing import Optional
from pydantic import BaseModel


class Docs(BaseModel):
    swagger_url: Optional[str] = None
    redoc_url: Optional[str] = None 
    openapi_url: Optional[str] = None
