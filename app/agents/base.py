from abc import ABC, abstractmethod

class Agent(ABC):
    @abstractmethod
    async def run(self, **kwargs):
        raise NotImplementedError
