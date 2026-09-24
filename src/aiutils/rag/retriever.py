import logging

from aiutils.embeddings.base import EmbeddingProvider
from aiutils.embeddings.similarity import cosine_similarity
from aiutils.rag.document import Document

logger = logging.getLogger(__name__)


class Retriever:

    def __init__(
        self,
        embedding_provider: EmbeddingProvider,
    ) -> None:
        self.embedding_provider = embedding_provider

    def retrieve(
        self,
        query: str,
        documents: list[Document],
        top_k: int = 3,
    ) -> list[Document]:
        """Return the most relevant documents for a query."""

        logger.info("Retrieving documents for query")

        query_embedding = self.embedding_provider.embed(query)

        scored_documents = []

        for document in documents:
            document_embedding = self.embedding_provider.embed(
                document.content
            )

            score = cosine_similarity(
                query_embedding,
                document_embedding,
            )

            scored_documents.append((score, document))

        scored_documents.sort(
            key=lambda item: item[0],
            reverse=True,
        )

        results = [
            document
            for score, document in scored_documents[:top_k]
        ]

        logger.info("Retrieved %d documents", len(results))

        return results