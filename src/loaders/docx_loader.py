"""
Production-quality DOCX document loader.
"""

from pathlib import Path

from docx import Document

from src.loaders.base_loader import BaseLoader


class DocxLoader(BaseLoader):
    """
    Loads textual content from DOCX documents.
    """

    def load(self, file_path: str | Path) -> str:
        """
        Load a DOCX document and return its extracted text.
        """

        path = Path(file_path)

        if not path.exists():
            self.logger.error("DOCX file not found: %s", path)
            raise FileNotFoundError(f"File not found: {path}")

        if path.suffix.lower() != ".docx":
            self.logger.error("Invalid DOCX file: %s", path)
            raise ValueError(f"Expected a DOCX file, got: {path.suffix}")

        self.logger.info("Loading DOCX: %s", path)

        try:
            document = Document(path)

            paragraphs = [
                paragraph.text.strip()
                for paragraph in document.paragraphs
                if paragraph.text.strip()
            ]

            text = "\n".join(paragraphs).strip()

            if not text:
                self.logger.warning("No text extracted from DOCX: %s", path)
                raise ValueError("No text could be extracted from the DOCX.")

            self.logger.info(
                "Successfully loaded DOCX '%s' (%d paragraphs)",
                path.name,
                len(paragraphs),
            )

            return text

        except Exception as exc:
            self.logger.exception("Failed to load DOCX: %s", path)
            raise RuntimeError(f"Failed to load DOCX '{path.name}'") from exc