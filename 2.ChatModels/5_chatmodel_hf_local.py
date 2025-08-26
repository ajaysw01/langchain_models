from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

model_id = "mistralai/Mistral-7B-Instruct-v0.3"

llm = HuggingFacePipeline.from_model_id(
    model_id=model_id,
    task="text_generation",
    pipeline_kwargs=dict(temperature=0.5, max_new_tokens=100),
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of India")
print(result.content)
