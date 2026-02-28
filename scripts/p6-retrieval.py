# Phase 6: Vector Database Retrieval (ZenBook/MX150 Optimized)

import chromadb
from chromadb.utils import embedding_functions
import os

def run_retrieval_logic(user_query=None):
    # 1. Setup Absolute Path to 'vector-db'
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, "vector-db") 
    
    # 2. MX150 optimized local embedding [cite: 2026-02-23]
    emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )

    # 3. Connect to the actual persistence directory
    client = chromadb.PersistentClient(path=db_path)
    
    try:
        collection = client.get_collection(
            name="infra_sentinel_index", 
            embedding_function=emb_fn
        )
    except Exception as e:
        return f"Database Retrieval Error: {str(e)}"

    # 4. Handle default query if none passed from Orchestrator
    if user_query is None:
        user_query = "Expert in Linux and Docker"

    # 5. Execute Semantic Search
    results = collection.query(
        query_texts=[user_query],
        n_results=2
    )

    # 6. Return formatted context for Phase 9
    documents = results.get('documents', [[]])[0]
    combined_context = "\n---\n".join(documents)
    
    return combined_context

if __name__ == "__main__":
    # Standalone Test logic
    print("DEBUG: Starting Standalone Retrieval Test...")
    print(run_retrieval_logic())
