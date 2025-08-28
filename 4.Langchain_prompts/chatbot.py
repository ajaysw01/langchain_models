from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model_id = "meta-llama/Llama-3.1-8B-Instruct"
llm = HuggingFaceEndpoint(
    repo_id=model_id, task="text-generation"
)

model = ChatHuggingFace(llm=llm)
#Version 1 :
#Problem : The bot does not remember the conversation history.
# while True:
#     user_input = input('You:')
#     if user_input == 'exit':
#         break
#     result = model.invoke(user_input)
#     print("BOT: ", result.content)

#Version 2 :
#Problem : If the chat history gets too big, the model or also we will not able to tell which messages is whose.
# chat_history = []
# while True:
#     user_input = input('You:')
#     chat_history.append(user_input)
#     if user_input == 'exit':
#         break
#     result = model.invoke(chat_history)
#     chat_history.append(result.content)
#     print("BOT: ", result.content)
#
# print(chat_history)


# Version 3 :

chat_history = [
    SystemMessage(content="Your are helpful AI assistant.")
]
while True:
    user_input = input('You:')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("BOT: ", result.content)

print(chat_history)
