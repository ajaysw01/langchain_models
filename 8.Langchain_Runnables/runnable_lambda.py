from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_ollama import ChatOllama
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(model="llama3:latest", temperature=0)
parser = StrOutputParser()

def word_counter(text):
    return len(text.split())

prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)
joke_gen_chain = RunnableSequence(prompt, llm, parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    # 'word_count': RunnableLambda(word_counter)),
    'word_count': RunnableLambda(lambda x : len(x.split()))
})

chain = RunnableSequence(joke_gen_chain,parallel_chain)

print(chain.invoke({'topic':'AI'}))