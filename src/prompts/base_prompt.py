"""
Base prompt class.
"""

from abc import ABC, abstractmethod


class BasePrompt(ABC):
    """
    Abstract base class for all prompt templates.
    """

    @abstractmethod
    def build(self, user_input: str) -> str:
        """
        Build the prompt.

        Args:
            user_input: User question.

        Returns:
            Formatted prompt.
        """
        pass