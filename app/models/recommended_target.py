from pydantic import BaseModel

class RecommendedTarget(BaseModel):
   language: str
   framework: str