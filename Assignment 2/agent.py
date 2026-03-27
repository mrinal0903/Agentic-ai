from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

def create_llm():
    pipe = pipeline(
        "text-generation",      # ✅ stable task
        model="gpt2",           # ✅ compatible free model
        max_new_tokens=300,     # ✅ avoids length error
        temperature=0.7,        # ✅ better output variation
        do_sample=True          # ✅ improves generation
    )

    llm = HuggingFacePipeline(pipeline=pipe)
    return llm
