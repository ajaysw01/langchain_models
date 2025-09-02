from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(model="llama3:latest", temperature=0)

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke -  {text}',
    input_variables=['text']
)
parser = StrOutputParser()

chain = RunnableSequence(prompt1, llm, parser, prompt2,llm,parser)

print(chain.invoke({'topic':'AI'}))