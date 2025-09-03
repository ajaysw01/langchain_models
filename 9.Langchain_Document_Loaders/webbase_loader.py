from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(model="llama3:latest", temperature=0)

prompt= PromptTemplate(
    template='Answer the following question \n {question} from the following text -\n {text}',
    input_variables=['question','text']
)
parser = StrOutputParser()


url = 'https://en.wikipedia.org/wiki/Robert_Greene_(American_author)'

loader = WebBaseLoader(url)
docs = loader.load()
# print(docs)

chain = prompt | llm | parser
chain.invoke({"question": "Who is Robert Greene?",
              "text": docs[0].page_content})