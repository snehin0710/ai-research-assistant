"""
Production-quality PDF document loader.
"""

from pathlib import Path

from pypdf import PdfReader

from src.loaders.base_loader import BaseLoader


class PDFLoader(BaseLoader):
    """
    Loads textual content from PDF documents.
    """

    def load(self, file_path: str | Path) -> str:
        """
        Load a PDF document and return its extracted text.

        Args:
            file_path:
                Path to the PDF file.

        Returns:
            Extracted text as a single string.

        Raises:
            FileNotFoundError:
                If the file does not exist.

            ValueError:
                If the file is not a PDF or no text could be extracted.

            RuntimeError:
                If PDF parsing fails.
        """

        path = Path(file_path)

        if not path.exists():
            self.logger.error("PDF file not found: %s", path)
            raise FileNotFoundError(f"File not found: {path}")

        if path.suffix.lower() != ".pdf":
            self.logger.error("Invalid PDF file: %s", path)
            raise ValueError(f"Expected a PDF file, got: {path.suffix}")

        self.logger.info("Loading PDF: %s", path)

        try:
            reader = PdfReader(path)

            pages: list[str] = []

            for page_number, page in enumerate(reader.pages, start=1):
                text = page.extract_text()

                if text:
                    pages.append(text)
                else:
                    self.logger.warning(
                        "Skipping empty page %d in %s",
                        page_number,
                        path.name,
                    )

            document = "\n".join(pages).strip()

            if not document:
                self.logger.warning("No text extracted from PDF: %s", path)
                raise ValueError("No text could be extracted from the PDF.")

            self.logger.info(
                "Successfully loaded PDF '%s' (%d pages with text)",
                path.name,
                len(pages),
            )

            return document

        except Exception as exc:
            self.logger.exception("Failed to load PDF: %s", path)
            raise RuntimeError(f"Failed to load PDF '{path.name}'") from exc