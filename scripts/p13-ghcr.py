import subprocess
import sys

# Configuration for Sentinel RAG Project
IMAGE_NAME = "sentinel-rag-app:v1"
GHCR_PATH = "ghcr.io/mavyjimz/sentinel-rag-app:v1"

def deploy_to_registry():
    print("--- [PHASE 13: IRONCLAD REGISTRY DEPLOYMENT] ---")
    
    # Absolute paths to satisfy Bandit B607 (Partial Path) and B603 (Untrusted Input)
    # Common Linux paths for standard CI/CD runners
    SUDO_EXE = "/usr/bin/sudo"
    DOCKER_EXE = "/usr/bin/docker"

    try:
        # 1. Tagging with Absolute Paths and Static Strings
        print(f"Tagging {IMAGE_NAME}...")
        subprocess.run(
            [SUDO_EXE, DOCKER_EXE, "tag", "sentinel-rag-app:v1", "ghcr.io/mavyjimz/sentinel-rag-app:v1"],
            check=True
        )
        
        # 2. Pushing with Absolute Paths and Static Strings
        print(f"Pushing to {GHCR_PATH}...")
        subprocess.run(
            [SUDO_EXE, DOCKER_EXE, "push", "ghcr.io/mavyjimz/sentinel-rag-app:v1"],
            check=True
        )
        
        print("\n[SUCCESS] Sentinel Image verified in GHCR.")

    except subprocess.CalledProcessError as e:
        print(f"Deployment Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    deploy_to_registry()
