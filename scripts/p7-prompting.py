# Phase 7: Prompt Template Engineering
# Objective: Guide the LLM to answer only based on the retrieved Sentinel knowledge base.

def get_sentinel_prompt(context, query):
    system_prompt = f"""
    You are the "Infra-Sentinel," a highly specialized MLOps Assistant.
    Your knowledge is STRICTLY limited to the technical profiles provided in the context below.
    
    RULES:
    1. If the answer is not in the context, say "I do not have information on this in my current profile database."
    2. Do not use outside knowledge or hallucinate.
    3. Keep responses professional and technical.
    
    CONTEXT:
    {context}
    
    USER QUERY:
    {query}
    
    SENTINEL RESPONSE:
    """
    return system_prompt

# Test the template
if __name__ == "__main__":
    sample_context = "Profile: Vanjunn, Role: MLOps Architect, Skills: Linux, Docker, Python."
    sample_query = "What are Vanjunn's skills?"
    print(get_sentinel_prompt(sample_context, sample_query))
