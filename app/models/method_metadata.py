from pydantic import BaseModel, Field
from typing import List, Optional
from app.models.parameter_metadata import ParameterMetadata
class MethodMetadata(BaseModel):
   name: str
   return_type: Optional[str] = Field(default="void", alias="returnType")
   visibility: Optional[str] = "public"
   summary: Optional[str] = None
   parameters: List[ParameterMetadata] = []

   class Config:
       populate_by_name = True