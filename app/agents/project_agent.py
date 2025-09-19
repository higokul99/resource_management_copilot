from .base import Agent

class ProjectAgent(Agent):
    async def run(self, profile_summary: dict):
        # match to open projects (stubbed)
        return {"projects": [{"id": 123, "name": "Cloud Migration"}]}
