import os
from kaggle.api.kaggle_api_extended import KaggleApi

def run_ingestion():
    api = KaggleApi()
    api.authenticate()
    
    # Verified slug from your browser search
    dataset = "imshiva10/stack-overflow-developer-survey-2022"
    
    # 1. Get the absolute path of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Go up one level to the project root
    project_root = os.path.dirname(script_dir)
    
    # 3. Target the specific raw folder inside the project
    target_path = os.path.join(project_root, "input-data", "raw")
    
    print(f"Phase 1: Ingesting {dataset}...")
    print(f"Targeting Project Folder: {target_path}")
    
    # This command downloads and unzips directly into your internal project folder
    api.dataset_download_files(dataset, path=target_path, unzip=True)
    
    print("Phase 1: Success. Data is now correctly inside the project folder.")

if __name__ == "__main__":
    run_ingestion()
