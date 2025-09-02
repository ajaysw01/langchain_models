from typing import Literal
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda

load_dotenv()

llm = ChatOllama(model="llama3:latest", temperature=0)

