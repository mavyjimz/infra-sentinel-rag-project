# infra-sentinel-rag
Enterprise-grade Retrieval-Augmented Generation (RAG) infrastructure for technical documentation.

## Project Overview
This repository implements a 20-phase MLOps lifecycle designed for industrial technical data. Developed over a high-velocity 7-day sprint (Feb 25 - Mar 3, 2026), the architecture is optimized for hardware-constrained environments (8GB RAM / MX150 GPU) and focuses on security-hardened containerization and automated system observability.

## Technical Specifications
* **CI/CD**: Multi-workflow automation via GitHub Actions with integrated Bandit security auditing.
* **Containerization**: 4.02 GB image deployment to GitHub Container Registry (GHCR).
* **Monitoring**: Real-time health checks for Vector DB latency (~500ms) and model availability.
* **Storage**: Persistent ChromaDB instance with automated state management.
* **FinOps**: Resource profiling confirmed at ~12.93 MB RAM footprint for core query logic.

## MLOps Lifecycle (20-Phase Roadmap)
| Phase | Milestone | Status | Technical Detail |
| :--- | :--- | :--- | :--- |
| 1-12 | Infrastructure Core | Completed | Raw ingestion to automated RAG API. |
| 13-14 | CI/CD & Security | Completed | GHCR integration and Bandit security gating. |
| 15 | Observability | Completed | Automated health monitoring and latency tracking. |
| 16 | Feedback Loop | Deferred | Strategic deferment for Independent R&D. |
| 17 | FinOps | Completed | Standalone resource profiling (MX150/8GB). |
| 18 | Career Portability | Completed | Repository documentation and portfolio audit. |
| 19 | System Hardening | Completed | Local environment sanitization and maintenance. |
| 20 | Disaster Recovery | Completed | Automated ChromaDB state-point backup/restoration. |



## Architectural Decisions
* **Strategic Deferment**: Phase 16 was deferred to prioritize hardware-specific profiling (Phase 17). This ensured the 4.02 GB footprint remained optimized for 8GB environments before establishing external feedback bridges.
* **Batch Deployment**: Final operational phases (17-20) were developed and verified locally to optimize CI/CD runner efficiency and reduce build-cycle overhead.

## Quick Start
To execute the system health monitoring suite:
```bash
python3 scripts/p15-monitoring.py
