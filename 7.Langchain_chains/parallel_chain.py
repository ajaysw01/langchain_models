from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

# input as document we will generate notes and quzi
llm1 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    max_new_tokens=256,
    temperature=0.5
)
llm2 = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    max_new_tokens=256,
    temperature=0.3
)

model1 = ChatHuggingFace(llm=llm1)
model2 = ChatHuggingFace(llm=llm2)

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n{text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question and answers from the following text \n{text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes ---> {notes} and quiz --->{quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

#parallel chains
parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
})

#merge part
merge_chain = prompt3 |model1 | parser
chain = parallel_chain | merge_chain

result = chain.invoke({'text':'An MCP server is a lightweight program that exposes specific tools, data sources, or actions to AI agents via the Model Context Protocol, acting like a smart adapter that translates AI requests into concrete operations (e.g., calling APIs, reading files, querying databases), advertises its capabilities for discovery, enforces permissions, manages sessions and context, and returns structured results over standardized channels (commonly JSON-RPC via stdio or HTTP/SSE), enabling modular, secure, reusable integrations so multiple clients can reliably access local or remote resources without custom glue code, much like a universal “USB-C” port for AI tool access.'})

print(result)

chain.get_graph().print_ascii()
