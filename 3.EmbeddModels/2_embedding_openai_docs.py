from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    model='text-embedding-3-large', 
    dimensions=32
)

documents = [
    "Delhi is the capital of India.",
    "Gandhinagar is the captial of Gujarat.",
    "Paris is the capital of France."
]

result = embeddings.embed_documents(documents)

print(str(result))
