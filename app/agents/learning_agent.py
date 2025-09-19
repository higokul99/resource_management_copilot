from .base import Agent

class LearningAgent(Agent):
    async def run(self, skills: list):
        # call LLM / RAG to recommend certifications
        return {"courses": ["AWS Certified DevOps Engineer", "GCP Professional"]}
