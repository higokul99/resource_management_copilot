from .base import Agent

class ProfileAgent(Agent):
    async def run(self, user_id: int, db=None):
        # load user profile from DB and extract skills
        return {"skills": ["python", "aws", "java"], "aspirations": ["lead engineer"]}
