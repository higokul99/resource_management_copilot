from .base import Agent

class MentorAgent(Agent):
    async def run(self, user_skills: list):
        # find mentors by skills, experience
        return {"mentors": [{"id": 9, "name": "Priya"}]}
