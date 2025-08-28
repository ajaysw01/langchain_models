from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate([
    ('system','Your are a helpful {domain} expert'),
    ('human','Explain in simple terms , what is {topic}')
])

# chat_template = ChatPromptTemplate.from_messages([
#     ('system','Your are a helpful {domain} expert'),
#     ('human','Explain in simple terms , what is {topic}')
# ]) old syntax

prompt = chat_template.invoke({'domain':'cricket', 'topic': 'batting'})
print(prompt)