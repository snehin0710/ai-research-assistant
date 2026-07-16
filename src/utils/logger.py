import logging
import sys
from pathlib import Path

LOG_DIR = Path("logs")

LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"

def get_logger(name: str = "AI Research Assistant"):
    logger = logging.getLogger(name)

    if logger.handlers:
       return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    console_handler = logging.StreamHandler(sys.stdout)

    console_handler.setLevel(logging.INFO)

    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(LOG_FILE)

    file_handler.setLevel(logging.INFO)

    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    logger.addHandler(file_handler)

    return logger