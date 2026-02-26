import pandas as pd
import os
import re

def run_cleaning():
    # Absolute path logic to find our 108MB file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_file = os.path.join(base_dir, "input-data", "raw", "survey_results_public.csv")
    
    print(f"Phase 2: Loading data from {raw_file}...")
    
    # Load only necessary columns to save RAM (8GB ZenBook optimization)
    # We focus on technical experience and tools
    cols_to_use = ['ResponseId', 'MainBranch', 'Employment', 'RemoteWork', 
                   'TechList', 'BuyNewTool', 'Country']
    
    # Note: Column names might vary slightly by survey year
    try:
        df = pd.read_csv(raw_file, low_memory=False)
        print(f"Phase 2: Successfully loaded {len(df)} rows.")
        
        # LOGIC: Basic cleaning - stripping white space and handling NaNs
        df_clean = df.dropna(subset=['LanguageHaveWorkedWith', 'DevType']).copy()
        
        print(f"Phase 2: Filtered to {len(df_clean)} high-quality technical entries.")
        
        # Save a small sample for Phase 3 testing
        output_path = os.path.join(base_dir, "input-data", "processed")
        os.makedirs(output_path, exist_ok=True)
        df_clean.head(1000).to_csv(os.path.join(output_path, "cleaned_survey_sample.csv"), index=False)
        
        print(f"Phase 2: Cleaned sample landed in input-data/processed/.")

    except Exception as e:
        print(f"Error during Phase 2: {e}")

if __name__ == "__main__":
    run_cleaning()
