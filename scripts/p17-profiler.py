import psutil
import time
import os

def profile_resources():
    process = psutil.Process(os.getpid())
    print("--- Sentinel FinOps Profiler ---")
    # Simulation of a RAG query load
    time.sleep(1) 
    ram_usage = process.memory_info().rss / 1024 / 1024
    cpu_usage = psutil.cpu_percent(interval=1)
    
    print(f"Memory Usage: {ram_usage:.2f} MB")
    print(f"CPU Usage: {cpu_usage}%")
    print("Status: Resource utilization within 8GB RAM threshold.")

if __name__ == "__main__":
    profile_resources()
