import logging
from pathlib import Path


LOG_FILE = Path("aiutils_logs.txt")


def setup_logging() -> None:
    """Configure logging for the aiutils package."""

    logger = logging.getLogger("aiutils")

    if logger.handlers:
        return

    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8",
    )

    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.propagate = False


def get_logger(name: str) -> logging.Logger:
    """Return a logger for an aiutils module."""

    setup_logging()

    return logging.getLogger(name)