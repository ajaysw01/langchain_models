from typing import Literal
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda

load_dotenv()

llm = ChatOllama(model="llama3:latest", temperature=0)

class Review(BaseModel):
    sentiment: Literal['Positive', 'Negative'] = Field(
        description="Give the sentiment of the review"
    )

parser = PydanticOutputParser(pydantic_object=Review)
parser1 = StrOutputParser()

prompt1 = PromptTemplate(
    template="Classify the following review text into Positive or Negative:\n{review}\n{format_instructions}",
    input_variables=["review"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive review:\n{review}",
    input_variables=["review"],
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative review:\n{review}",
    input_variables=["review"],
)

classifier_chain = prompt1 | llm | parser

branch_chain = RunnableBranch(
    (lambda x: x["sentiment"] == "Positive", prompt2 | llm | parser1),
    (lambda x: x["sentiment"] == "Negative", prompt3 | llm | parser1),
    RunnableLambda(lambda x: "No sentiment detected"),
)

chain = {
    "review": lambda x: x["review"],
    "sentiment": lambda x: classifier_chain.invoke({"review": x["review"]}).sentiment,
} | branch_chain

result = chain.invoke({"review": "The product quality is excellent and I am very satisfied with my purchase."})
print(result)