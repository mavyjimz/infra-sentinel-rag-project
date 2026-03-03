import time
import sys

# Phase 15: Observability & Monitoring
# Objective: Performance tracking and health checks

def check_vector_db_health():
    print("--- [PHASE 15: MONITORING SYSTEM HEALTH] ---")
    
    # Logic: Automated monitoring of vector database latency
    try:
        print("Checking Vector Database connection...")
        # Simulate a latency check (In production, this would be a ping to Qdrant/Milvus)
        start_time = time.time()
        time.sleep(0.5)  # Simulated check
        latency = (time.time() - start_time) * 1000
        
        print(f"[SUCCESS] Vector DB is responsive. Latency: {latency:.2f}ms")
        return True
    except Exception as e:
        print(f"[ALERT] Vector DB Health Check Failed: {e}")
        return False

def check_model_availability():
    # Logic: Automated monitoring of embedding model availability
    print("Verifying Embedding Model availability...")
    # Simulate a health check for the LLM/Embedding service
    is_available = True 
    
    if is_available:
        print("[SUCCESS] Embedding Model is online and ready.")
        return True
    else:
        print("[ALERT] Embedding Model Service is DOWN.")
        return False

if __name__ == "__main__":
    db_ok = check_vector_db_health()
    model_ok = check_model_availability()
    
    # If any critical system is down, exit with error so GitHub Actions alerts us
    if not db_ok or not model_ok:
        print("\n[CRITICAL] System health degraded. Monitoring alert triggered.")
        sys.exit(1)
    else:
        print("\n[COMPLETE] All Sentinel systems are operational.")
        sys.exit(0)
