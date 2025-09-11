from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnablePassthrough
from langchain_ollama import ChatOllama
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(model="llama3:latest", temperature=0)

prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)
parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1, llm, parser)
branch_chain = RunnableBranch(
    # (conditon, runnable),
    (lambda x : len(x.split())>200, RunnableSequence(prompt2, llm, parser)),
    RunnablePassthrough()
)

chain = RunnableSequence(report_gen_chain, branch_chain)

print(chain.invoke({'topic':'Russia vs Ukraine'}))