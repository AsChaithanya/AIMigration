from fastapi import APIRouter
from app.models.migration_request import MigrationRequest
from app.agent.migration_agent import MigrationAgent

router = APIRouter(
   prefix="/migration",
   tags=["Migration"]
)
agent = MigrationAgent()

@router.post("/execute")
def execute(request: MigrationRequest):
   return agent.execute(request)