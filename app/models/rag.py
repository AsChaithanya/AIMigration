from typing import List
from pydantic import BaseModel
from app.models.rag_document import RagDocument

class Rag(BaseModel):
   documents: List[RagDocument]