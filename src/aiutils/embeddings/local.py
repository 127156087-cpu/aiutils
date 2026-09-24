import logging

from sentence_transformers import SentenceTransformer

from aiutils.embeddings.base import EmbeddingProvider

logger = logging.getLogger(__name__)


class LocalEmbeddingProvider(EmbeddingProvider):

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2",
    ) -> None:

        self.model = SentenceTransformer(model_name)

        logger.info("Embedding model initialized")

    def embed(self, text: str) -> list[float]:
        """Convert text into a semantic embedding vector."""

        logger.debug("Creating embedding")

        embedding = self.model.encode(text)

        return embedding.tolist()