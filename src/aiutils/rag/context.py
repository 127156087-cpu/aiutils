import logging

from aiutils.llm import LLMClient, LLMResponse
from aiutils.rag.document import Document

logger = logging.getLogger(__name__)


def build_context(documents: list[Document]) -> str:
    """Combine documents into a single context string."""

    logger.info("Building context from %d documents", len(documents))

    context_parts = []

    for document in documents:
        context_parts.append(document.content)

    context = "\n\n".join(context_parts)

    logger.debug("Context created")

    return context


def generate_answer(
    question: str,
    documents: list[Document],
    llm_client: LLMClient,
) -> LLMResponse:
    """Generate an answer using documents as context."""

    logger.info("Generating answer using retrieved context")

    context = build_context(documents)

    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{question}
"""

    response = llm_client.generate(prompt)

    logger.info("Answer generated")

    return response