# Phase 11: Security & API Vaulting
# Objective: Harden the pipeline by managing secrets

import os
from dotenv import load_dotenv

def load_sentinel_secrets():
    # Load the hidden .env file from the root directory
    load_dotenv()
    
    user = os.getenv("KAGGLE_USERNAME")
    key = os.getenv("KAGGLE_KEY")
    db_path = os.getenv("SENTINEL_DB_PATH")
    
    print("--- [PHASE 11: SECURITY CHECK] ---")
    
    if user and key:
        print("Status: Kaggle Credentials Loaded Safely.")
    else:
        print("Error: Kaggle Credentials Missing in .env")
        
    if db_path:
        print(f"Status: Secure DB Path set to: {db_path}")
    else:
        print("Error: SENTINEL_DB_PATH not found in .env")
        
    return {"user": user, "key": key, "db": db_path}

if __name__ == "__main__":
    load_sentinel_secrets()
