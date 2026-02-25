# infra-sentinel-rag-project: Master Workflow Guide

## Phase 1: Data Ingestion (p1-ingestion.py)
* **Objective**: Establish a secure handshake with Kaggle for the Stack Overflow Technical Q&A dataset [cite: 2026-01-10].
* **Logic**: Automate zip download/extraction to `input-data/raw/` using authenticated Kaggle API [cite: 2026-02-23, 2026-02-25].

## Phase 2: Text Cleaning & Normalization (p2-cleaning.py)
* **Objective**: Prepare messy technical text for vectorization.
* **Logic**: Use Regex to strip HTML tags while preserving code snippets and technical keywords [cite: 2026-02-25].

## Phase 3: Document Chunking (p3-chunking.py)
* **Objective**: Segment text into manageable pieces for the LLM context window.
* **Logic**: Implement RecursiveCharacterTextSplitter to ensure logical "Infrastructure" context is not cut in half [cite: 2026-02-25].

## Phase 4: Embedding Generation (p4-embedding.py)
* **Objective**: Convert text into mathematical vectors.
* **Logic**: Use a lightweight model (like Sentence-Transformers) optimized for the MX150 GPU [cite: 2026-02-23, 2026-02-25].

## Phase 5: Vector Database Setup (p5-vector-db.py)
* **Objective**: Persist vectors for fast retrieval.
* **Logic**: Initialize and configure ChromaDB within the `vector-db/` directory [cite: 2026-02-25].

## Phase 6: Retrieval Logic (p6-retrieval.py)
* **Objective**: Find the most relevant context for a user query.
* **Logic**: Build a similarity search engine that ranks document chunks by relevance [cite: 2026-02-25].

## Phase 7: Prompt Template Engineering (p7-prompting.py)
* **Objective**: Guide the LLM to answer only based on the retrieved "Sentinel" knowledge base.
* **Logic**: Design strict system prompts to prevent hallucinations [cite: 2026-02-25].

## Phase 8: Offline LLM Integration (p8-inference.py)
* **Objective**: Generate the final technical answer.
* **Logic**: Handshake with Ollama (Llama-3 or Phi-3) to run inference locally on your i5 system [cite: 2026-01-08, 2026-02-23].

## Phase 9: RAG Chain Orchestration (p9-orchestrator.py)
* **Objective**: Combine Retrieval, Prompting, and Generation into one automated pipeline [cite: 2026-01-15].
* **Logic**: Use LangChain to tie all previous phases into a unified "Sentinel" agent [cite: 2026-02-25].

## Phase 10: Evaluation & Validation (p10-evaluation.py)
* **Objective**: Measure the accuracy of the Sentinel's answers.
* **Logic**: Compare generated output against "Ground Truth" labels from the dataset.

## Phase 11: Security & API Vaulting (p11-security.py)
* **Objective**: Harden the pipeline for production.
* **Logic**: Manage Kaggle credentials and local API keys via environment variables and GitHub Secrets.

## Phase 12: Containerization (p12-dockerfile)
* **Objective**: Build a portable environment for the RAG system.
* **Logic**: Create a multi-stage Dockerfile to house the vector DB and Python logic [cite: 2026-01-27, 2026-02-24].

## Phase 13: Registry Deployment (p13-ghcr.py)
* **Objective**: Push the containerized Sentinel to the cloud.
* **Logic**: Automate the push to GitHub Container Registry (GHCR).

## Phase 14: CI/CD Automation (p14-github-actions)
* **Objective**: Ensure the pipeline stays "Green" with every push [cite: 2026-01-27].
* **Logic**: Finalize YAML workflows to trigger builds and tests automatically [cite: 2026-02-24].
