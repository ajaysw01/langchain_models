from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

model_id = "meta-llama/Llama-3.1-8B-Instruct"

# Define the base LLM
llm = HuggingFaceEndpoint(
    repo_id=model_id,
    task="text-generation"
)

# Wrap in chat interface
chat_model = ChatHuggingFace(llm=llm)
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me about LangChain"),
]

result = chat_model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)
