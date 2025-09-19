from fastapi import FastAPI
from app.api.v1 import health, auth, agents
from app.core.config import settings

app = FastAPI(title="GenAI Resource Co-pilot", version="0.1")

app.include_router(health.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")
app.include_router(agents.router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    # connect to DB, cache, load models, etc.
    print("Starting up: load embeddings and initialize agents")

@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down")
