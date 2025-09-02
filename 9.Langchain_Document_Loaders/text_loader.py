from langchain_community.document_loaders import TextLoader
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(model="llama3:latest", temperature=0)

prompt= PromptTemplate(
    template='write a summary for the following text - \n{text}',
    input_variables=['text']
)
parser = StrOutputParser()

loader = TextLoader('example.txt', encoding='utf-8')
docs = loader.load()
print(docs)
print(type(docs))
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)

chain = prompt | llm | parser

print(chain.invoke({'text':docs[0].page_content}))