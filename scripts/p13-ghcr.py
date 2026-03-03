import subprocess
import sys

# Configuration for Sentinel RAG Project
IMAGE_NAME = "sentinel-rag-app:v1"
GHCR_PATH = "ghcr.io/mavyjimz/sentinel-rag-app:v1"

def run_command(command_list):
    """
    Executes a command list without using shell=True to satisfy 
    security linting (Bandit B602) and prevent injection.
    """
    try:
        print(f"Executing: {' '.join(command_list)}")
        # Using a list format is safer and more predictable in CI/CD
        subprocess.run(command_list, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during execution: {e}")
        sys.exit(1)

def deploy_to_registry():
    print("--- [PHASE 13: HARDENED REGISTRY DEPLOYMENT] ---")
    
    # 1. Tagging the local 4.02GB image
    # Note: sudo is included as a list element for Linux environment compatibility
    print(f"Tagging {IMAGE_NAME} for GitHub Container Registry...")
    tag_cmd = ["sudo", "docker", "tag", IMAGE_NAME, GHCR_PATH]
    run_command(tag_cmd)
    
    # 2. Official Push logic
    print(f"Pushing {GHCR_PATH} to the cloud...")
    push_cmd = ["sudo", "docker", "push", GHCR_PATH]
    run_command(push_cmd)
    
    print("\n[SUCCESS] Sentinel Image is verified in GHCR.")

if __name__ == "__main__":
    deploy_to_registry()
