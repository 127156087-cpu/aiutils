from aiutils.llm import GroqProvider, LLMClient


def test_real_llm_client() -> None:
    provider = GroqProvider()

    client = LLMClient(provider)

    response = client.generate(
        "Explain what RAG is in one sentence."
    )

    assert response.text
    assert len(response.text) > 0