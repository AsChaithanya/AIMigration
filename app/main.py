from fastapi import FastAPI
from app.api.migration_api import router as migrationRouter
app = FastAPI(
   title="AI Migration Platform"
)
app.include_router(migrationRouter)

@app.get("/")
def health():
   return {
       "status": "Running"
   }