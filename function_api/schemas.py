#schemas.py
from pydantic import BaseModel

class ItemCreateRequest(BaseModel):
    name: str
    description: str

class ItemUpdateRequest(BaseModel):
    name: str
    description: str
