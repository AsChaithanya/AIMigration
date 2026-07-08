from pydantic import BaseModel
from typing import List
from app.models.class_metadata import ClassMetadata

class FileMetadata(BaseModel):
   name: str
   path: str
   package: str
   language: str

   imports: List[str] = []
   classes: List[ClassMetadata]