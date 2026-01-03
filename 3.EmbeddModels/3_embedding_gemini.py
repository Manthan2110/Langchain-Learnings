from langchain_google_genai import GoogleGenerativeAIEmbeddings

embedding = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key="YOUR_GOOGLE_API_KEY"
)

vector = embedding.embed_query("Gandhinagar is capital of Gujarat.")
print(str(vector))

