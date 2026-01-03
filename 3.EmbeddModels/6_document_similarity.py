from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

document = [
    "Sachin Tendulkar is regarded as the greatest batsman of all time, inspiring generations with his unmatched consistency and humility.",
    "Virat Kohli is known for his aggressive mindset and exceptional batting skills, setting new benchmarks in all formats of the game.",
    "MS Dhoni is celebrated as one of the best captains in cricket history, famous for his calm leadership and finishing abilities.",
    "Rohit Sharma is admired for his elegant batting and record-breaking double centuries in One Day Internationals.",
    "Jasprit Bumrah is India’s pace spearhead, feared worldwide for his deadly yorkers and unorthodox bowling action."
]

query = "Tell me about Jasprit."

doc_embeddings = embedding.embed_documents(document)
query_embeddings = embedding.embed_query(query)

Scores = cosine_similarity([query_embeddings], doc_embeddings)[0]
index, score = sorted(list(enumerate(Scores)), key= lambda x:x[1])[-1]

print(query)
print(document[index])
print("Similarity score is :", score)