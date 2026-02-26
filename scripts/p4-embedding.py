import pandas as pd
import os
import chromadb
from chromadb.utils import embedding_functions

def run_embedding():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    chunk_file = os.path.join(base_dir, "input-data", "processed", "technical_chunks.csv")
    
    # CHANGED: Updated to use the hyphenated 'vector-db' folder
    db_path = os.path.join(base_dir, "vector-db")

    print(f"Phase 4: Generating embeddings from {chunk_file}...")

    try:
        df = pd.read_csv(chunk_file)
        
        # Initialize Persistent Client at the correct folder
        client = chromadb.PersistentClient(path=db_path)
        
        model_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
        
        collection = client.get_or_create_collection(
            name="infra_sentinel_index", 
            embedding_function=model_func
        )

        print("Phase 4: Encoding and indexing...")

        collection.add(
            documents=df['technical_chunk'].tolist(),
            ids=df['ResponseId'].astype(str).tolist()
        )

        print(f"Phase 4: Success! Vectors merged into {db_path}.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_embedding()
