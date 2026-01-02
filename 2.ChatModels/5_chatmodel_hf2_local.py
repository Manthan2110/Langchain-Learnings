from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
import os

os.environ['HF_HOME'] = "M:/LangChain/LangChain_Models/huggingface_cache"

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task = "text-generation",
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_new_tokens = 100
    )
)
model = ChatHuggingFace(llm=llm)
print(model.invoke("What is the captial of India???").content)