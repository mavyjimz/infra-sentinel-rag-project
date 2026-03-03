# Phase 11: Security & API Vaulting (Hardened for Phase 14)
# Objective: Manage secrets for Kaggle and DB paths securely.

import os
from dotenv import load_dotenv
import sys

def load_sentinel_secrets():
    # Load .env only if it exists (local dev). 
    # In GitHub Actions, secrets are injected directly into environment variables.
    if os.path.exists(".env"):
        load_dotenv()
    
    print("--- [PHASE 11: SECURITY CHECK] ---")

    # 1. Fetching Credentials
    user = os.getenv("KAGGLE_USERNAME")
    key = os.getenv("KAGGLE_KEY")
    db_path = os.getenv("SENTINEL_DB_PATH")

    # 2. Validation Logic with Graceful Exit
    if user and key:
        print("Status: Kaggle Credentials Loaded Safely.")
    else:
        # In CI/CD, we don't want to crash, but we need to warn
        print("Warning: Kaggle Credentials Missing in Environment.")

    if db_path:
        print(f"Status: Secure DB Path set to: {db_path}")
    else:
        # Default to a relative path if missing to avoid "Denied" errors
        db_path = "input-data/processed/technical_chunks.csv"
        print(f"Status: Using default relative DB path: {db_path}")

    return {"user": user, "key": key, "db": db_path}

if __name__ == "__main__":
    try:
        secrets = load_sentinel_secrets()
    except Exception as e:
        print(f"Security Vault Error: {e}")
        sys.exit(1)
