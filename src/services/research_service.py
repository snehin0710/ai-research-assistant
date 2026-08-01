"""
Research service.
"""

from src.core.exceptions import AIProviderError
from src.prompts.research_prompt import ResearchPrompt
from src.services.openai_client import OpenAIClient


class ResearchService:
    """
    Service responsible for generating AI research responses.
    """

    def __init__(self) -> None:
        self.client = OpenAIClient()
        self.prompt = ResearchPrompt()

    def research(self, query: str) -> str:
        """
        Generate a research response.

        Args:
            query: User's research question.

        Returns:
            AI-generated answer.
        """

        prompt = self.prompt.build(query)

        try:
            return self.client.generate_response(prompt)

        except AIProviderError:
            raise

    def close(self) -> None:
        """
        Release resources.
        """

        self.client.close()