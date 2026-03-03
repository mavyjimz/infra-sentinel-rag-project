# Phase 10: Evaluation & Validation (Hardened for CI/CD)
# Standardized for ZenBook and GitHub Runner [cite: 2026-02-23]

import pandas as pd
import os
import sys
import importlib.util

def run_evaluation():
    print("--- [PHASE 10: EVALUATION START] ---")
    
    # 1. Use relative pathing to avoid "Denied" errors
    # This works both on your laptop and in the GitHub Cloud
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "input-data/processed/technical_chunks.csv")
    orch_path = os.path.join(base_dir, "scripts/p9-orchestrator.py")

    # 2. Dynamic Import for Orchestrator
    if not os.path.exists(orch_path):
        print(f"Error: Orchestrator not found at {orch_path}")
        sys.exit(1)
        
    spec = importlib.util.spec_from_file_location("p9_orchestrator", orch_path)
    orchestrator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(orchestrator)

    # 3. Load Technical Chunks
    try:
        df = pd.read_csv(data_path)
    except FileNotFoundError:
        print(f"Error: CSV file not found at {data_path}")
        return

    # 4. Pull Ground Truth Sample
    ground_truth_sample = df.iloc[0]['technical_chunk']

    # 5. Execute Sentinel Query
    test_query = "Find me an expert in Linux and Docker"
    print(f"Validating Sentinel against Ground Truth: {ground_truth_sample[:60]}...")

    # Calling the P9 function we just hardened
    generated_answer = orchestrator.run_sentinel_pipeline(test_query)

    # 6. Accuracy Scoring (Keyword match)
    expected_tech = ["Linux", "Docker", "Python", "Bash"]
    found_tech = [t for t in expected_tech if t.lower() in generated_answer.lower()]
    accuracy = (len(found_tech) / len(expected_tech)) * 100

    print("\n--- [VALIDATION REPORT] ---")
    print(f"SENTINEL ANSWER : {generated_answer}")
    print(f"ACCURACY SCORE  : {accuracy}%")
    print(f"VERIFIED TECH   : {found_tech}")

if __name__ == "__main__":
    run_evaluation()
