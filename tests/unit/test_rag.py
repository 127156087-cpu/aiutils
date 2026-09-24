from aiutils.rag.document import Document
from aiutils.rag.retriever import Retriever
from aiutils.rag.context import build_context


class FakeEmbeddingProvider:

    def embed(self, text: str) -> list[float]:
        if "Python" in text:
            return [1.0, 0.0]

        return [0.0, 1.0]


def test_document() -> None:
    document = Document(
        content="Python is a programming language.",
        metadata={"source": "notes.txt"},
    )

    assert document.content == "Python is a programming language."
    assert document.metadata["source"] == "notes.txt"


def test_retriever() -> None:
    provider = FakeEmbeddingProvider()

    retriever = Retriever(provider)

    documents = [
        Document(content="Python is a programming language."),
        Document(content="Cooking recipes are useful."),
    ]

    results = retriever.retrieve(
        query="Python",
        documents=documents,
        top_k=1,
    )

    assert len(results) == 1
    assert results[0].content == "Python is a programming language."


def test_build_context() -> None:
    documents = [
        Document(content="Python is a programming language."),
        Document(content="Python is used for AI."),
    ]

    context = build_context(documents)

    assert "Python is a programming language." in context
    assert "Python is used for AI." in context