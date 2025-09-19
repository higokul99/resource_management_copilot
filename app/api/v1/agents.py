from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.agents.orchestrator import Orchestrator

router = APIRouter()

class RecommendRequest(BaseModel):
    user_id: int
    intent: str | None = None

@router.post('/recommend')
async def recommend(req: RecommendRequest):
    orches = Orchestrator()
    result = await orches.recommend(user_id=req.user_id, intent=req.intent)
    return result
