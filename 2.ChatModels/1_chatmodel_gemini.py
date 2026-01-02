from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    google_api_key="YOUR_GOOGLE_API_KEY",
    temperature= 0
)

print(model.invoke("What is captial of india??").content)