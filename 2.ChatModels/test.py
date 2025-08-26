from langchain_huggingface import HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="gpt2",
    task="text-generation"
)

print(llm.invoke("Hello, how are you today?"))
