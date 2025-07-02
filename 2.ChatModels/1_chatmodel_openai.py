from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI chat model
chat_model = ChatOpenAI(model="gpt-4", temperature=0, max_completion_tokens=10)
result = chat_model.invoke("what is the capital of india ?")
print(result.content)
