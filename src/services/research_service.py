"""
Research service.
"""

from src.core.exceptions import AIProviderError
from src.services.openai_client import OpenAIClient


class ResearchService:
    """
    Service responsible for generating AI research responses.
    """

    def __init__(self) -> None:
        self.client = OpenAIClient()

    def research(self, query: str) -> str:
        """
        Generate a research response.

        Args:
            query: User's research question.

        Returns:
            AI-generated answer.
        """

        prompt = f"""
You are an expert AI Research Assistant.

Your job is to produce answers that are:

- Accurate
- Well-structured
- Easy to understand
- Factually correct
- Professional

Research Question:
{query}
"""

        try:
            return self.client.generate_response(prompt)

        except AIProviderError:
            raise

    def close(self) -> None:
        """
        Release resources.
        """

        self.client.close()