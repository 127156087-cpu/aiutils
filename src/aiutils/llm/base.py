import logging
from abc import ABC, abstractmethod
from getpass import getpass

from groq import Groq

logger = logging.getLogger(__name__)


class LLMProvider(ABC):

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a response from a prompt."""
        pass


class MockLLMProvider(LLMProvider):

    def generate(self, prompt: str) -> str:
        """Return a fake response for testing."""
        logger.debug("Generating mock LLM response")
        return f"Mock response for: {prompt}"


class GroqProvider(LLMProvider):

    def __init__(
        self,
        api_key: str | None = None,
        model: str = "openai/gpt-oss-120b",
    ) -> None:

        self.model = model

        if not api_key:
            api_key = getpass("Enter api key:")

        if not api_key:
            raise ValueError("Groq API key cannot be empty")

        self.client = Groq(api_key=api_key)

        logger.info("Groq provider initialized")

    def generate(self, prompt: str) -> str:
        """Generate a response using Groq."""

        logger.info("Sending request to Groq")

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        content = response.choices[0].message.content

        if content is None:
            raise ValueError("LLM response content is empty")

        return content