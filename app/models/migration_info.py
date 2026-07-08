from typing import List, Optional
from pydantic import BaseModel

from app.models.recommended_target import RecommendedTarget
class MigrationInfo(BaseModel):
   source_framework: str
   recommended_targets: List[RecommendedTarget]
   ui_type: str
   migration_complexity: str
   confidence: float
   migration_type: Optional[str] = None