from pydantic import BaseModel, Field

class Relationship(BaseModel):
   from_class: str = Field(alias="from")
   to_class: str = Field(alias="to")
   type: str
   model_config = {
       "populate_by_name": True
   }