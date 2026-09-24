import logging

logger = logging.getLogger(__name__)


class MemoryCache:

    def __init__(self) -> None:
        self.cache: dict[str, str] = {}

        logger.debug("Memory cache initialized")

    def set(self, key: str, value: str) -> None:
        """Store a value in the cache."""

        self.cache[key] = value

        logger.debug("Value stored in cache")

    def get(self, key: str) -> str | None:
        """Get a value from the cache."""

        value = self.cache.get(key)

        if value is None:
            logger.debug("Cache miss")
        else:
            logger.debug("Cache hit")

        return value

    def delete(self, key: str) -> None:
        """Delete a value from the cache."""

        self.cache.pop(key, None)

        logger.debug("Value removed from cache")

    def clear(self) -> None:
        """Clear all cached values."""

        self.cache.clear()

        logger.debug("Cache cleared")