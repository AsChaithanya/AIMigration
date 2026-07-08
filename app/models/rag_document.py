from pydantic import BaseModel

class RagDocument(BaseModel):
   id: str
   type: str
   content: str