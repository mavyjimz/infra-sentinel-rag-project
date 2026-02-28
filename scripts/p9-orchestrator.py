# Phase 9: RAG Chain Orchestration (Hyphen-Safe Version)

import requests
import json
import sys
import os
import importlib.util

# 1. Setup paths to find our scripts
base_dir = os.path.dirname(os.path.abspath(__file__))

def import_hyphenated_module(module_name, path):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# 2. Dynamic Imports for hyphenated files
p7 = import_hyphenated_module("p7_prompting", os.path.join(base_dir, "p7-prompting.py"))
p6 = import_hyphenated_module("p6_retrieval", os.path.join(base_dir, "p6-retrieval.py"))

def run_sentinel_pipeline(user_query):
    print(f"\n[ORCHESTRATOR] Processing Query: {user_query}")
    
    # RETRIEVE: Calling p6-retrieval.py
    context_results = p6.run_retrieval_logic(user_query) 
    
    # PROMPT: Calling p7-prompting.py
    full_prompt = p7.get_sentinel_prompt(context_results, user_query)
    
    # GENERATE: Local Ollama (MX150/CUDA) [cite: 2026-02-23]
    url = "http://localhost:11434/api/generate"
    payload = {"model": "qwen", "prompt": full_prompt, "stream": False}
    
    try:
        response = requests.post(url, json=payload)
        return response.json().get('response', "Pipeline Error.")
    except Exception as e:
        return f"Orchestration Error: {str(e)}"

if __name__ == "__main__":
    test_query = "Find me an expert in Linux and Docker."
    final_answer = run_sentinel_pipeline(test_query)
    print(f"\nSENTINEL FINAL ANSWER:\n{final_answer}")
