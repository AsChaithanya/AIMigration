from pydantic import BaseModel

class FileInfo(BaseModel):
   name: str
   path: str
   package: str
   language: str