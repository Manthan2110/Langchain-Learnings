from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv(override=True)

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task = "text-generation",
    max_new_tokens= 50
)

model = ChatHuggingFace(llm=llm)

print(model.invoke("What is the capital of India?").content)