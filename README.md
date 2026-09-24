# aiutils

A typed Python toolkit for common AI and LLM application tasks.

`aiutils` provides simple, reusable utilities for:

* Text cleaning
* Text chunking
* Tokenization
* Text embeddings
* Cosine similarity
* LLM providers
* LLM client with retry support
* Response models
* In-memory caching
* RAG document retrieval
* Context building

The project is built using Python, type hints, Pydantic, pytest, and modular package design.

## Project Status

This project is currently under development.

The core text, embedding, LLM, cache, and RAG components have been implemented and tested.

## Requirements

* Python 3.11 or newer
* A Groq API key for the real LLM integration

## Installation

Clone the repository:

```bash
git clone https://github.com/127156087-cpu/aiutils
cd aiutils
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Install the package in editable mode:

```bash
python -m pip install -e .
```

## Basic Usage

### Text Utilities

```python
from aiutils import clean_text, chunk_text, tokenize

text = "  Hello    Python   World  "

cleaned = clean_text(text)
tokens = tokenize(cleaned)
chunks = chunk_text(cleaned, chunk_size=2)

print(cleaned)
print(tokens)
print(chunks)
```

### Embeddings

```python
from aiutils import LocalEmbeddingProvider

embedding_provider = LocalEmbeddingProvider()

embedding = embedding_provider.embed(
    "Python is a programming language."
)

print(embedding)
```

### Similarity

```python
from aiutils import cosine_similarity

vector_a = [1.0, 0.0]
vector_b = [1.0, 0.0]

similarity = cosine_similarity(
    vector_a,
    vector_b,
)

print(similarity)
```

### RAG

```python
from aiutils import (
    Document,
    LocalEmbeddingProvider,
    Retriever,
    build_context,
)

documents = [
    Document(
        content="Python is a programming language.",
        metadata={"source": "python.txt"},
    ),
    Document(
        content="RAG combines retrieval with language models.",
        metadata={"source": "rag.txt"},
    ),
]

embedding_provider = LocalEmbeddingProvider()

retriever = Retriever(embedding_provider)

results = retriever.retrieve(
    query="What is RAG?",
    documents=documents,
    top_k=1,
)

context = build_context(results)

print(context)
```

### LLM

The package includes a Groq provider.

```python
from aiutils import GroqProvider, LLMClient

provider = GroqProvider(
    api_key="YOUR_GROQ_API_KEY"
)

client = LLMClient(provider)

response = client.generate(
    "Explain what RAG is in one sentence."
)

print(response.text)
```

Do not commit API keys to GitHub or store them directly in source code.


## End-to-End Demo

The project includes a temporary `run_demo.py` script that demonstrates how the main components of `aiutils` work together.

The demo performs the following steps:

1. Creates sample documents
2. Generates embeddings for the documents
3. Retrieves the most relevant document using cosine similarity
4. Builds a context from the retrieved document
5. Sends the context to the Groq LLM
6. Generates an answer
7. Stores the response in the in-memory cache

Before running the demo, make sure you have installed the dependencies and package:

```bash
python -m pip install -r requirements.txt
python -m pip install -e .

### Cache

```python
from aiutils import MemoryCache

cache = MemoryCache()

cache.set("name", "Python")

value = cache.get("name")

print(value)
```

## Testing

Run the unit tests:

```bash
python -m pytest tests/unit
```

Run the integration tests:

```bash
python -m pytest tests/integration -s
```

The integration test communicates with the real Groq API and requires a valid API key.


## Test Coverage

The project uses `pytest-cov` to measure test coverage.

Run the test suite with coverage using:

```bash
python -m pytest --cov=aiutils --cov-report=term-missing


## Project Structure

```text
aiutils/
├── pyproject.toml
├── README.md
├── LICENSE
├── CHANGELOG.md
├── .gitignore
├── requirements.txt
│
├── src/
│   └── aiutils/
│       ├── __init__.py
│       ├── exceptions.py
│       ├── config.py
│       ├── logging.py
│       │
│       ├── text/
│       ├── embeddings/
│       ├── prompts/
│       ├── llm/
│       ├── rag/
│       └── cache/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
│
└── .github/
    └── workflows/
        └── ci.yml
```


## Logging

aiutils uses Python's built-in logging system.

When the package is used, runtime logs are written to:

aiutils_logs.txt

The log file is generated automatically and is excluded from version control.

Logs contain useful information about package operations such as:
- text processing
- embedding generation
- document retrieval
- LLM requests
- cache operations
- retry attempts

Sensitive information such as API keys and private user content is not logged.


## Development

The project uses:

* Type hints for clearer interfaces
* Pydantic for data validation
* pytest for testing
* Mocking for isolated unit tests
* Logging for application diagnostics
* A `src` layout for package development
* Editable installation during development

Additional development tools such as Ruff, Mypy, coverage, and GitHub Actions will be added as development continues.

## License

This project is licensed under the MIT License.
