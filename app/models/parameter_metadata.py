from pydantic import BaseModel
class ParameterMetadata(BaseModel):
   name: str
   type: str