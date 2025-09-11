from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Define the LLM
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    max_new_tokens=256,
    temperature=0.3
)

model = ChatHuggingFace(llm=llm)

# Define schema
schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 facts about {about}\n{format_instruction}',
    input_variables=['about'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# Build chain
chain = template | model | parser

# Call chain
result = chain.invoke({'about': 'black hole'})
print(result)
