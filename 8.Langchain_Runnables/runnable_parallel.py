from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(model="llama3:latest", temperature=0)

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a LinkedIn post about {topic}',
    input_variables=['topic']
)
parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet' : RunnableSequence(prompt1, llm, parser),
    'linkedin_post' : RunnableSequence(prompt2, llm, parser)
})

result = parallel_chain.invoke({'topic' : 'Ai'})

print(result['tweet'])
print(result['linkedin_post'])