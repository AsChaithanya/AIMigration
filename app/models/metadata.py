from pydantic import BaseModel

class Metadata(BaseModel):
   project_name: str
   language: str
   framework: str
   build_tool: str
   source_version: str
   target_version: str
   target_language: str
   target_framework: str
   files: int