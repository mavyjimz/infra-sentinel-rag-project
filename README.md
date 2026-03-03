# infra-sentinel-rag
Enterprise-grade Retrieval-Augmented Generation (RAG) infrastructure for technical documentation.

## Project Overview
This repository implements a 20-phase MLOps lifecycle designed for industrial technical data. The architecture is optimized for hardware-constrained environments (8GB RAM / MX150 GPU) and focuses on security-hardened containerization and automated system observability.

## Technical Specifications
* CI/CD: Multi-workflow automation (GitHub Actions) with integrated Bandit security auditing.
* Containerization: 4.02 GB image deployment via GitHub Container Registry (GHCR).
* Monitoring: Real-time health checks for Vector DB latency (~500ms) and model availability.
* Storage: Persistent ChromaDB instance with automated state management.

## MLOps Lifecycle (20-Phase Roadmap)
This project follows a structured engineering blueprint to ensure system reliability and career portability.

| Phase | Milestone | Status | Technical Detail |
| :--- | :--- | :--- | :--- |
| 1-14 | Infrastructure Core | Completed | Raw ingestion to automated CI/CD deployment. |
| 15 | Observability | Completed | Automated health checks for system latency. |
| 16 | Continuous Improvement| Deferred | Strategic deferment for Independent R&D. |
| 17 | FinOps | In-Progress | Hardware-specific resource profiling (RAM/GPU). |
| 18 | Career Portability | Completed | Repository alignment and portfolio optimization. |
| 19 | System Hardening | Pending | IaC-based secret scanning and maintenance. |
| 20 | Disaster Recovery | Pending | Automated state backup and restoration protocols. |



## Architectural Decisions
The project utilizes "Strategic Deferment" for Phase 16 to prioritize Phase 17 (FinOps). This ensures the 4.02 GB footprint is resource-optimized for 8GB environments before establishing external feedback bridges. This decision-making process mimics production-level resource allocation in enterprise AI environments.

## Quick Start
To execute the system health monitoring suite:
```bash
python3 scripts/p15-monitoring.py
