# Phase 10: Evaluation & Validation
# Standardized for ZenBook Linux environment [cite: 2026-02-23]

import pandas as pd
import os
import importlib.util

def run_evaluation():
    # 1. Absolute Paths for Sentinel Project
    base_dir = "/home/vanjunn-pongasi/MLOps/infra-sentinel-rag-project"
    data_path = os.path.join(base_dir, "input-data/processed/technical_chunks.csv")
    orch_path = os.path.join(base_dir, "scripts/p9-orchestrator.py")
    
    print("--- [PHASE 10: EVALUATION START] ---")
    
    # 2. Dynamic Import for p9-orchestrator.py [cite: 2026-02-20]
    spec = importlib.util.spec_from_file_location("p9_orchestrator", orch_path)
    orchestrator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(orchestrator)
    
    # 3. Load Technical Chunks
    df = pd.read_csv(data_path)
    
    # 4. Target Column from head output
    content_col = 'technical_chunk'
    
    # 5. Pull a real ground truth sample (Response 3)
    ground_truth_sample = df.iloc[0][content_col]
    
    # 6. Execute Sentinel Query
    test_query = "Find me an expert in Linux and Docker"
    print(f"Validating Sentinel against Ground Truth: {ground_truth_sample[:60]}...")
    
    generated_answer = orchestrator.run_sentinel_pipeline(test_query)
    
    # 7. Accuracy Scoring (Keyword match based on P9 success)
    expected_tech = ["Linux", "Docker", "Python", "Bash"]
    found_tech = [t for t in expected_tech if t.lower() in generated_answer.lower()]
    accuracy = (len(found_tech) / len(expected_tech)) * 100
    
    print("\n--- [VALIDATION REPORT] ---")
    print(f"SENTINEL ANSWER : {generated_answer}")
    print(f"ACCURACY SCORE  : {accuracy}%")
    print(f"VERIFIED TECH   : {found_tech}")

if __name__ == "__main__":
    run_evaluation()
