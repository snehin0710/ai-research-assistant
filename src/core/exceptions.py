"""
Custom exceptions for the AI Research Assistant.
"""


class AIResearchAssistantError(Exception):
    """Base exception for the application."""


class AIProviderError(AIResearchAssistantError):
    """Raised when an AI provider returns an error."""


class AuthenticationError(AIProviderError):
    """Raised when authentication with the AI provider fails."""


class RateLimitError(AIProviderError):
    """Raised when the rate limit is exceeded."""


class ProviderUnavailableError(AIProviderError):
    """Raised when the AI provider is unavailable."""


class InvalidResponseError(AIProviderError):
    """Raised when the AI provider returns an invalid response."""