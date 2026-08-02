"""
Production-quality text document loader.
"""

from pathlib import Path

from src.loaders.base_loader import BaseLoader


class TextLoader(BaseLoader):
    """
    Loads plain text documents.
    """

    def load(self, file_path: str | Path) -> str:
        """
        Load a text document.
        """

        path = Path(file_path)

        if not path.exists():
            self.logger.error("Text file not found: %s", path)
            raise FileNotFoundError(f"File not found: {path}")

        if path.suffix.lower() != ".txt":
            self.logger.error("Invalid text file: %s", path)
            raise ValueError(f"Expected a TXT file, got: {path.suffix}")

        self.logger.info("Loading text file: %s", path)

        try:
            text = path.read_text(encoding="utf-8").strip()

            if not text:
                self.logger.warning("Empty text file: %s", path)
                raise ValueError("Text file is empty.")

            self.logger.info("Successfully loaded text file: %s", path.name)

            return text

        except Exception as exc:
            self.logger.exception("Failed to load text file: %s", path)
            raise RuntimeError(f"Failed to load text file '{path.name}'") from exc