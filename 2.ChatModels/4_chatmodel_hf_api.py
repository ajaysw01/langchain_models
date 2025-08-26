from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

model_id = "meta-llama/Llama-3.1-8B-Instruct"
llm = HuggingFaceEndpoint(
    repo_id=model_id, task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)
