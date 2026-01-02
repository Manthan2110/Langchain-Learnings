from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(
    model= "claude-3-5-sonnet-20241022", 
    temperature=0.4, 
    max_tokens_to_sample=5
)

#I don't have enough money to recharge anthropic tokens.
print(model.invoke("Who is the No.1 male batsman as per ICC Cricket Ranking??").content)