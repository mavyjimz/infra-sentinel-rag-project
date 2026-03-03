import subprocess
import sys

# Configuration for Sentinel RAG Project
IMAGE_NAME = "sentinel-rag-app:v1"
GHCR_PATH = "ghcr.io/mavyjimz/sentinel-rag-app:v1"

def deploy_to_registry():
    print("--- [PHASE 13: HARDENED REGISTRY DEPLOYMENT] ---")
    
    try:
        # 1. Tagging (Static strings to satisfy Bandit B603)
        print(f"Tagging {IMAGE_NAME}...")
        subprocess.run(
            ["sudo", "docker", "tag", "sentinel-rag-app:v1", "ghcr.io/mavyjimz/sentinel-rag-app:v1"],
            check=True
        )
        
        # 2. Pushing (Static strings to prevent untrusted input flags)
        print(f"Pushing to {GHCR_PATH}...")
        subprocess.run(
            ["sudo", "docker", "push", "ghcr.io/mavyjimz/sentinel-rag-app:v1"],
            check=True
        )
        
        print("\n[SUCCESS] Sentinel Image verified in GHCR.")

    except subprocess.CalledProcessError as e:
        print(f"Deployment Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    deploy_to_registry()
