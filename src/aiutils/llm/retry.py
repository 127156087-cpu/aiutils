import logging
import time

logger = logging.getLogger(__name__)


def retry(
    function,
    attempts: int = 3,
    delay: float = 1.0,
):
    """Retry a function when it raises an exception."""

    for attempt in range(1, attempts + 1):
        try:
            return function()

        except Exception as error:
            logger.warning(
                "Attempt %d/%d failed: %s",
                attempt,
                attempts,
                error,
            )

            if attempt == attempts:
                raise

            time.sleep(delay)