import subprocess
import sys

# Configuration for Sentinel RAG Project
IMAGE_NAME = "sentinel-rag-app:v1"
GHCR_PATH = "ghcr.io/mavyjimz/sentinel-rag-app:v1"

def run_command(command):
    try:
        print(f"Executing: {command}")
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during execution: {e}")
        sys.exit(1)

def deploy_to_registry():
    print("--- [PHASE 13: REGISTRY DEPLOYMENT] ---")
    
    # Tagging the local 4.02GB image for GHCR
    print(f"Tagging {IMAGE_NAME} for GitHub Container Registry...")
    run_command(f"sudo docker tag {IMAGE_NAME} {GHCR_PATH}")
    
    # Official Push command logic
    print(f"Pushing {GHCR_PATH} to the cloud...")
    run_command(f"sudo docker push {GHCR_PATH}")
    
    print("\n[SUCCESS] Sentinel Image is verified in GHCR.")

if __name__ == "__main__":
    deploy_to_registry()
