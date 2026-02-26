import os
import chromadb
from chromadb.utils import embedding_functions

def run_retrieval_logic():
    # Use absolute pathing for ZenBook environment reliability
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, "vector-db")

    print("Phase 6: Initializing Semantic Retrieval Engine...")

    try:
        # 1. Connect to the persistent ChromaDB store
        client = chromadb.PersistentClient(path=db_path)
        
        # 2. Use the same MX150 optimized model from Phase 4/5 [cite: 2026-02-23]
        model_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
        collection = client.get_collection(name="infra_sentinel_index", embedding_function=model_func)

        # 3. Define a technical query to test logic
        user_query = "Find me developers with strong experience in Docker, Kubernetes, and Python"
        print(f"Searching for: {user_query}")

        # 4. Perform Similarity Search (Retrieve top 2 matches)
        results = collection.query(
            query_texts=[user_query],
            n_results=2
        )

        # 5. Display the retrieved context
        print("\n--- Top Retrieved Technical Context ---")
        for i, document in enumerate(results['documents'][0]):
            print(f"Match {i+1}: {document}\n")

    except Exception as e:
        print(f"Phase 6 Error: {e}")

if __name__ == "__main__":
    run_retrieval_logic()
