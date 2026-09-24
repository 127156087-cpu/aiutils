from unittest.mock import Mock

from aiutils.llm import LLMClient


def test_llm_client() -> None:
    provider = Mock()

    provider.generate.return_value = "Mocked LLM response"

    client = LLMClient(provider)

    response = client.generate(
        "Explain Python."
    )

    assert response.text == "Mocked LLM response"

    provider.generate.assert_called_once_with(
        "Explain Python."
    )