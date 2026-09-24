from aiutils.embeddings import cosine_similarity


def test_cosine_similarity() -> None:
    vector_a = [1.0, 0.0]
    vector_b = [1.0, 0.0]

    result = cosine_similarity(vector_a, vector_b)

    assert result == 1.0


def test_different_vectors() -> None:
    vector_a = [1.0, 0.0]
    vector_b = [0.0, 1.0]

    result = cosine_similarity(vector_a, vector_b)

    assert result == 0.0