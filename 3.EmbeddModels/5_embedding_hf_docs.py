from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Delhi is the capital of India.",
    "Gandhinagar is the capital of Gujarat.",
    "Paris is the capital of France."
]
vector = embeddings.embed_documents(documents)
print(str(vector))