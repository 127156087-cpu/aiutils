import logging

from aiutils.cache import MemoryCache
from aiutils.llm.base import LLMProvider
from aiutils.llm.response import LLMResponse
from aiutils.llm.retry import retry

logger = logging.getLogger(__name__)


class LLMClient:

    def __init__(
        self,
        provider: LLMProvider,
        retry_attempts: int = 3,
        retry_delay: float = 1.0,
        cache: MemoryCache | None = None,
    ) -> None:
        self.provider = provider
        self.retry_attempts = retry_attempts
        self.retry_delay = retry_delay
        self.cache = cache

    def generate(self, prompt: str) -> LLMResponse:
        """Generate a response using the configured provider."""

        logger.info("Generating LLM response")

        if self.cache:
            cached_response = self.cache.get(prompt)

            if cached_response is not None:
                logger.info("Returning cached response")

                return LLMResponse(
                    text=cached_response,
                    model=self.provider.__class__.__name__,
                )

        text = retry(
            lambda: self.provider.generate(prompt),
            attempts=self.retry_attempts,
            delay=self.retry_delay,
        )

        if self.cache:
            self.cache.set(prompt, text)
            logger.info("LLM response stored in cache")

        return LLMResponse(
            text=text,
            model=self.provider.__class__.__name__,
        )