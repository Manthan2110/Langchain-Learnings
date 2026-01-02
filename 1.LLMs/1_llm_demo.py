from langchain_google_genai import GoogleGenerativeAI

llm = GoogleGenerativeAI(
    model='gemini-2.5-flash',
    google_api_key="YOUR_GOOGLE_API_KEY"
)

result = llm.invoke("Who is the Prime Minister of India now")

print(result)
