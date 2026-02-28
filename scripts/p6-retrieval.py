# Phase 6: Vector Database Retrieval
# Objective: Search ChromaDB for relevant technical profiles based on a query.

import chromadb
from chromadb.utils import embedding_functions
import os

def run_retrieval_logic(user_query=None):
    # 1. Setup paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    persist_dir = os.path.join(base_dir, "..", "data", "chroma_db")
    
    # 2. Use local embedding model (Optimized for MX150/8GB RAM) [cite: 2026-02-23]
    emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )

    # 3. Connect to ChromaDB
    client = chromadb.PersistentClient(path=persist_dir)
    collection = client.get_collection(name="infra_sentinel_index", embedding_function=emb_fn)

    # 4. Handle default test query if none provided
    if user_query is None:
        user_query = "Expert in Linux and Docker"

    # 5. Execute Semantic Search
    results = collection.query(
        query_texts=[user_query],
        n_results=2
    )

    # 6. Format results for Phase 9 Orchestration
    context_list = results.get('documents', [[]])[0]
    combined_context = "\n---\n".join(context_list)
    
    # Return for Phase 9, print for manual testing
    if __name__ == "__main__":
        print(f"DEBUG RETRIEVAL FOR: {user_query}")
        print(combined_context)
        
    return combined_context

if __name__ == "__main__":
    run_retrieval_logic()
