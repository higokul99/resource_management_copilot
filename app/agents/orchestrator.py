from .profile_agent import ProfileAgent
from .learning_agent import LearningAgent
from .project_agent import ProjectAgent
from .mentor_agent import MentorAgent

class Orchestrator:
    def __init__(self):
        self.profile_agent = ProfileAgent()
        self.learning_agent = LearningAgent()
        self.project_agent = ProjectAgent()
        self.mentor_agent = MentorAgent()

    async def recommend(self, user_id: int, intent: str | None = None):
        profile = await self.profile_agent.run(user_id=user_id)
        learn = await self.learning_agent.run(skills=profile.get('skills', []))
        projects = await self.project_agent.run(profile_summary=profile)
        mentors = await self.mentor_agent.run(user_skills=profile.get('skills', []))

        return {
            'profile': profile,
            'learning': learn,
            'projects': projects,
            'mentors': mentors,
            'explanation': 'Aggregated by Orchestrator'
        }
