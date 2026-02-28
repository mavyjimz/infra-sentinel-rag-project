# Phase 6: Vector Database Retrieval (System Integration Version)
# Optimized for: i5 8th Gen / MX150 GPU / 8GB RAM

import chromadb
from chromadb.utils import embedding_functions
import os

def run_retrieval_logic(user_query=None):
    # 1. Setup Absolute Infrastructure Paths
    # Ensures the script finds 'vector-db' regardless of where it is called from
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, "vector-db") 
    
    # 2. Local Embedding Model (Zero API Cost / High Privacy)
    # Model: all-MiniLM-L6-v2 (Lightweight and Fast for MX150)
    emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )

    # 3. Connect to Persistent ChromaDB
    client = chromadb.PersistentClient(path=db_path)
    
    try:
        # Connect to the index created in Phase 5
        collection = client.get_collection(
            name="infra_sentinel_index", 
            embedding_function=emb_fn
        )
    except Exception as e:
        return f"Database Retrieval Error: {str(e)}"

    # 4. Handle Input (Default test query if none provided)
    if user_query is None:
        user_query = "Expert in Linux and Docker"

    # 5. Execute Semantic Search (Depth: 5 Results)
    # Increased from 2 to 5 to provide more 'Knowledge' to the LLM
    results = collection.query(
        query_texts=[user_query],
        n_results=5 
    )

    # 6. Format Context for the Sentinel (Phase 7 Prompt Compatibility)
    documents = results.get('documents', [[]])[0]
    
    # We add a clear boundary so the LLM parses separate profiles correctly
    combined_context = "\n\n--- [NEW PROFILE DATA] ---\n\n".join(documents)
    
    return combined_context

if __name__ == "__main__":
    # Standalone Test logic for manual verification
    print("--- [SENTINEL RETRIEVAL TEST] ---")
    print(f"Searching for: Expert in Linux and Docker")
    context_output = run_retrieval_logic()
    print(context_output)
