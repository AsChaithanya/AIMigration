from typing import List, Optional
from pydantic import BaseModel
from app.models.parameter_metadata import ParameterMetadata

class ConstructorMetadata(BaseModel):
   signature: Optional[str] = None
   modifier: Optional[str] = None
   parameters: List[ParameterMetadata] = []