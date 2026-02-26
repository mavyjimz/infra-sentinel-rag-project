import os
import chromadb
from chromadb.utils import embedding_functions

def setup_vector_db():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Standardizing to your hyphenated folder
    db_path = os.path.join(base_dir, "vector-db")

    print(f"Phase 5: Initializing ChromaDB at {db_path}...")

    try:
        # 1. Initialize Persistent Client
        client = chromadb.PersistentClient(path=db_path)
        
        # 2. Re-verify the Embedding Function [cite: 2026-02-23]
        model_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
        
        # 3. Access the collection created in Phase 4
        collection = client.get_or_create_collection(
            name="infra_sentinel_index", 
            embedding_function=model_func
        )

        # 4. Persistence Check
        vector_count = collection.count()
        print(f"Phase 5: Success! {vector_count} vectors are persisted and ready.")
        
        # 5. Peak at the structure (First item metadata)
        if vector_count > 0:
            sample = collection.peek(1)
            print("Database Health: Verified.")

    except Exception as e:
        print(f"Phase 5 Error: {e}")

if __name__ == "__main__":
    setup_vector_db()
