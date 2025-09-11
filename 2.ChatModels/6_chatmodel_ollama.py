from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3:latest", temperature=0)

result = llm.invoke("What is the capital of India")
print(result.content)

