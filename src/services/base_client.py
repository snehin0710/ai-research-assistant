"""
Base HTTP client for AI providers.
"""

from typing import Any

import httpx

from src.config import get_settings
from src.core.exceptions import (
    AIProviderError,
    AuthenticationError,
    ProviderUnavailableError,
    RateLimitError,
)
from src.utils.logger import get_logger


class BaseClient:
    """
    Base class for external AI provider clients.

    Responsibilities:
    - Manage HTTP client
    - Send HTTP requests
    - Handle common errors
    - Log requests/responses
    """

    def __init__(self, base_url: str) -> None:
        self.settings = get_settings()

        self.logger = get_logger(self.__class__.__name__)

        self.base_url = base_url

        self.client = httpx.Client(
            base_url=self.base_url,
            timeout=self.settings.REQUEST_TIMEOUT,
            headers={
                "Content-Type": "application/json",
            },
        )

    def post(
        self,
        endpoint: str,
        payload: dict[str, Any],
        headers: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        """
        Send a POST request.

        Args:
            endpoint: API endpoint.
            payload: JSON payload.
            headers: Optional request headers.

        Returns:
            Parsed JSON response.
        """

        self.logger.info("POST request to %s", endpoint)

        try:
            response = self.client.post(
                endpoint,
                json=payload,
                headers=headers,
            )

            response.raise_for_status()

            self.logger.info(
                "Request succeeded (%s)",
                response.status_code,
            )

            data = response.json()

            self.logger.debug("Response JSON parsed successfully")

            return data

        except httpx.HTTPStatusError as exc:

            status_code = exc.response.status_code

            self.logger.error(
                "HTTP error %s: %s",
                status_code,
                exc.response.text,
            )

            if status_code == 401:
                raise AuthenticationError(
                    "Authentication with AI provider failed."
                ) from exc

            if status_code == 429:
                raise RateLimitError(
                    "Rate limit exceeded."
                ) from exc

            if status_code >= 500:
                raise ProviderUnavailableError(
                    "AI provider is currently unavailable."
                ) from exc

            raise AIProviderError(
                f"Unexpected provider error ({status_code})."
            ) from exc

        except httpx.RequestError as exc:

            self.logger.error(
                "Network request failed: %s",
                str(exc),
            )

            raise ProviderUnavailableError(
                "Unable to connect to the AI provider."
            ) from exc

    def close(self) -> None:
        """
        Close the HTTP client.
        """

        self.client.close()