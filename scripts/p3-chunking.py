import pandas as pd
import os

def run_chunking():
    # Absolute path logic to locate the cleaned data [cite: 2026-02-02]
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    processed_dir = os.path.join(base_dir, "input-data", "processed")
    input_file = os.path.join(processed_dir, "cleaned_survey_sample.csv")
    
    print(f"Phase 3: Document Chunking - Reading from {input_file}...")
    
    try:
        # Load the cleaned data from Phase 2
        df = pd.read_csv(input_file)
        
        # LOGIC: Narrative Chunking
        # We synthesize multiple columns into a single searchable string
        def create_chunk(row):
            return (f"Response {row['ResponseId']}: A {row['DevType']} based in {row['Country']}. "
                    f"Proficient in: {row['LanguageHaveWorkedWith']}. "
                    f"Experience level: {row['YearsCode']} years of coding.")

        df['technical_chunk'] = df.apply(create_chunk, axis=1)
        
        # Save the finalized chunks for the Vector DB (Phase 4)
        output_file = os.path.join(processed_dir, "technical_chunks.csv")
        df[['ResponseId', 'technical_chunk']].to_csv(output_file, index=False)
        
        print(f"Phase 3: Success! Generated {len(df)} narrative chunks.")
        print(f"File saved to: {output_file}")

    except Exception as e:
        print(f"Error during Phase 3 processing: {e}")

if __name__ == "__main__":
    run_chunking()
