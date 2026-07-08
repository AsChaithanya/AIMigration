from pydantic import BaseModel
from typing import List, Optional
from app.models.field_metadata import FieldMetadata
from app.models.constructor_metadata import ConstructorMetadata
from app.models.method_metadata import MethodMetadata

class ClassMetadata(BaseModel):
   name: str
   type: str
   extends: Optional[str] = None
   implements: list[str] = []
   purpose: Optional[str] = None
   fields: List[FieldMetadata] = []
   constructors: List[ConstructorMetadata]
   methods: List[MethodMetadata] = []