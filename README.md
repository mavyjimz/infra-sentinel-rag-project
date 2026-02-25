# infra-sentinel-rag

**An Enterprise-Grade Retrieval-Augmented Generation (RAG) Pipeline for Infrastructure Technical Documentation.**

---

## Project Overview
This project demonstrates an end-to-end MLOps lifecycle designed to turn unstructured technical Q&A data (Stack Overflow) into a searchable, grounded Knowledge Base. It utilizes a Sentinel architecture to prevent LLM hallucinations by forcing responses to be grounded in verified documentation.

## Key Features
* Granular 14-Phase Pipeline: From raw Kaggle ingestion to automated GHCR deployment.
* Hardware Optimized: Engineered to run on 8GB RAM using quantized local embeddings.
* Offline-First: Supports local inference via Ollama (Llama-3/Phi-3) for data privacy.
* Production Logic: Implements vector similarity search (ChromaDB) and recursive text chunking.

## Tech Stack
* Language: Python 3.12 (venv-mlops)
* Orchestration: LangChain / Python-Dotenv
* Vector Store: ChromaDB
* Data Source: Kaggle API (Stack Overflow Q&A)
* Automation: GitHub Actions / Docker / GHCR

## MLOps Lifecycle (The Blueprint)
This project follows a strict 14-phase development cycle. For a deep-dive into the engineering logic of each phase, please refer to the MASTER_WORKFLOW_GUIDE.md.
