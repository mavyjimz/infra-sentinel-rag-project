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

## Phase 15: Observability & Monitoring (p15-monitoring.py)
* **Objective**: Implement system health checks and performance tracking.
* **Logic**: Automated monitoring of vector database latency and embedding model availability using GitHub Actions alerts.

## Phase 16: Continuous Improvement (p16-feedback.py)
* **Objective**: Establish a feedback loop for data evolution.
* **Logic**: Bridge GitHub Issues (human feedback) back to Phase 1 for automated re-ingestion of corrected technical data.

## Phase 17: FinOps & Resource Profiling (p17-profiler.py)
* **Objective**: Profile hardware consumption and optimize operational costs.
* **Logic**: Use a script to measure peak RAM usage during RAG retrieval and GPU utilization on the MX150.
* **Outcome**: Generate a "Cost-per-Query" report to justify infrastructure scaling or optimization needs.

## Phase 18: Documentation & Career Portability
* **Objective**: Consolidate technical lessons into a professional portfolio.
* **Logic**: Generate a final project summary linking 18 years of infrastructure experience to new MLOps skills.
* **Outcome**: A polished GitHub README and resume-ready documentation for recruitment.

## Phase 19: Security & Infrastructure-as-Code (p19-security.py)
* **Objective**: Hardening the pipeline and optimizing local resources.
* **Logic**: Script-based secret scanning to prevent token leaks and automated maintenance routines for the 8GB RAM environment.
* **Outcome**: A secure, self-cleaning MLOps environment.

## Phase 20: Disaster Recovery & State Backup
* **Objective**: Ensure project indestuctibility and business continuity.
* **Logic**: Automated state backup of the ChromaDB vector store and environment configurations.
* **Outcome**: Ability to restore the entire "Sentinel" ecosystem in minutes following hardware failure.
