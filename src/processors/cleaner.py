"""
Production-quality text cleaner.
"""

import re
import unicodedata


class TextCleaner:
    """
    Cleans extracted document text.
    """

    @staticmethod
    def clean(text: str) -> str:
        """
        Normalize and clean extracted text.
        """

        if not text:
            return ""

        # Unicode normalization
        text = unicodedata.normalize("NFKC", text)

        # Normalize line endings
        text = text.replace("\r\n", "\n").replace("\r", "\n")

        # Remove extra spaces and tabs
        text = re.sub(r"[ \t]+", " ", text)

        # Remove excessive blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()