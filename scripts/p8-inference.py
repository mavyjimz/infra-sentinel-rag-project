# Phase 8: Offline LLM Integration
# Objective: Send the engineered prompt to Ollama for local response generation.

import requests
import json

def query_sentinel(prompt):
    url = "http://localhost:11434/api/generate"
    
    # We will use 'qwen' or 'llama3' depending on your current setup [cite: 2026-01-09]
    payload = {
        "model": "qwen", 
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json().get('response', "No response received.")
    except Exception as e:
        return f"Error connecting to Ollama: {str(e)}"

if __name__ == "__main__":
    # Integration Test: Using the logic from Phase 7
    test_prompt = """
    You are the "Infra-Sentinel." 
    CONTEXT: Profile: Vanjunn, Role: MLOps Architect, Skills: Linux, Docker.
    USER QUERY: What can Vanjunn do?
    SENTINEL RESPONSE:
    """
    print("Sentinel is thinking...")
    answer = query_sentinel(test_prompt)
    print(f"\nFINAL ANSWER:\n{answer}")
