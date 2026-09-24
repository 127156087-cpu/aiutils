from aiutils import (
    Document,
    GroqProvider,
    LLMClient,
    LocalEmbeddingProvider,
    MemoryCache,
    Retriever,
    build_context,
)


def main() -> None:
    documents = [
        Document(
            content="Python is a high-level programming language.",
            metadata={"source": "python.txt"},
        ),
        Document(
            content="RAG combines retrieval with language models.",
            metadata={"source": "rag.txt"},
        ),
        Document(
            content="Machine learning allows computers to learn from data.",
            metadata={"source": "ml.txt"},
        ),
    ]

    embedding_provider = LocalEmbeddingProvider()

    retriever = Retriever(embedding_provider)

    question = "What is RAG?"

    relevant_documents = retriever.retrieve(
        query=question,
        documents=documents,
        top_k=2,
    )

    context = build_context(relevant_documents)

    print("\nRetrieved Context:")
    print(context)

    provider = GroqProvider()

    cache = MemoryCache()

    client = LLMClient(
        provider=provider,
        cache=cache,
    )

    prompt = f"""
Answer the question using the following context.

Context:
{context}

Question:
{question}
"""

    response = client.generate(prompt)

    print("\nLLM Response:")
    print(response.text)


if __name__ == "__main__":
    main()