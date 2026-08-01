"""
OpenAI-compatible client.

Currently configured to use the OpenRouter API.
"""

from src.config import get_settings
from src.services.base_client import BaseClient


class OpenAIClient(BaseClient):
    """
    Client for interacting with an OpenAI-compatible API.

    The current provider is OpenRouter, but because it exposes an
    OpenAI-compatible API, the client architecture remains the same.
    """

    def __init__(self) -> None:
        self.settings = get_settings()

        super().__init__(
            base_url="https://openrouter.ai/api/v1",
        )

        self.api_key = self.settings.OPENAI_API_KEY

    def generate_response(self, prompt: str) -> str:
        """
        Generate a response from the AI provider.
        """

        payload = {
            "model": self.settings.OPENAI_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are an expert AI Research Assistant. "
                        "Provide accurate, factual, and well-structured answers."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            "temperature": 0.3,
            "max_tokens": 1500,
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": "http://localhost:8501",
            "X-Title": self.settings.APP_NAME,
        }

        response = self.post(
            endpoint="/chat/completions",
            payload=payload,
            headers=headers,
        )

        try:
            choices = response.get("choices", [])

            if not choices:
                raise ValueError("No choices returned.")

            message = choices[0].get("message", {})

            content = message.get("content")

            if not content:
                raise ValueError("Model returned empty content.")

            return content.strip()

        except (KeyError, IndexError, ValueError) as exc:
            self.logger.error("Invalid response received: %s", response)
            raise RuntimeError(
                "Invalid response from AI provider."
            ) from exc