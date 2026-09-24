from aiutils.text import clean_text, chunk_text, tokenize


def test_clean_text() -> None:
    text = "  Hello    Python   World  "

    result = clean_text(text)

    assert result == "Hello Python World"


def test_chunk_text() -> None:
    text = "one two three four five"

    result = chunk_text(text, chunk_size=2)

    assert result == [
        "one two",
        "three four",
        "five",
    ]


def test_tokenize() -> None:
    text = "Hello Python World"

    result = tokenize(text)

    assert result == [
        "Hello",
        "Python",
        "World",
    ]