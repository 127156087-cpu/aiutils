# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows Semantic Versioning.

## [0.1.0] - 2026-09-23

### Added

* Initial `aiutils` Python package structure.
* Modern `src` package layout.
* Project configuration using `pyproject.toml`.
* Requirements management using `requirements.txt`.
* Custom `AIUtilsError` base exception.
* Basic application configuration using Pydantic.
* Logging utilities.
* Text cleaning utility.
* Text chunking utility.
* Basic text tokenization utility.
* Abstract `EmbeddingProvider` interface.
* Local embedding support using Sentence Transformers.
* Cosine similarity calculation.
* LLM provider abstraction.
* Mock LLM provider for testing.
* Groq LLM provider.
* LLM client with retry support.
* Pydantic `LLMResponse` model.
* In-memory cache.
* RAG `Document` model.
* RAG document retrieval using embeddings.
* RAG context building.
* LLM response generation using retrieved context.
* Unit tests for text, embeddings, LLM, RAG, and cache components.
* Integration test for the Groq LLM client.
* Logging across core components.

### Testing

* 10 unit tests passing.
* Real Groq integration test passing.
