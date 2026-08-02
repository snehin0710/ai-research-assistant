"""
Base document loader abstraction.

Every document loader must inherit from this class
and implement the load() method.
"""

from abc import ABC, abstractmethod
from pathlib import Path

from src.utils.logger import get_logger


class BaseLoader(ABC):
    """
    Abstract base class for document loaders.

    Concrete implementations are responsible for
    loading a document and returning its textual content.
    """

    def __init__(self) -> None:
        self.logger = get_logger(self.__class__.__name__)

    @abstractmethod
    def load(self, file_path: str | Path) -> str:
        """
        Load a document and return extracted text.

        Args:
            file_path:
                Path to the input document.

        Returns:
            Extracted document text.

        Raises:
            FileNotFoundError
            ValueError
            Exception
        """
        raise NotImplementedError