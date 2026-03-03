import requests
import json
import sys

# Phase 8: Offline LLM Integration
# Objective: Send the engineered prompt to Ollama with hardened security timeouts.

def query_sentinel(prompt):
    url = "http://localhost:11434/api/generate"
    
    # Configuration based on current setup [cite: 2026-01-09]
    payload = {
        "model": "qwen",
        "prompt": prompt,
        "stream": False
    }

    try:
        # Added timeout=30 to satisfy Bandit B113 and prevent CI/CD hangs
        response = requests.post(url, json=payload, timeout=30)
        response.raise_for_status()
        return response.json().get('response', "No response received.")
    
    except requests.exceptions.Timeout:
        return "Error: Connection to Ollama timed out after 30 seconds."
    except requests.exceptions.RequestException as e:
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
    try:
        answer = query_sentinel(test_prompt)
        print(f"\nFINAL ANSWER:\n{answer}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
