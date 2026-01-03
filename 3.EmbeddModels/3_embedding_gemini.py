from langchain_google_genai import GoogleGenerativeAIEmbeddings

embedding = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key="AIzaSyBNog1XNZTQDBctMWDc9cKNENA-tUfd0Bc"
)

vector = embedding.embed_query("Gandhinagar is capital of Gujarat.")
print(str(vector))
