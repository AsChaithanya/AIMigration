from typing import Optional
from pydantic import BaseModel

class FieldMetadata(BaseModel):
   name: str
   type: Optional[str] = None
   category: Optional[str] = None