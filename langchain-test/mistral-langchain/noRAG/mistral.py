from langchain_core.messages import HumanMessage
from langchain_mistralai.chat_models import ChatMistralAI
api_key="3GyMujRYXjA3Ti37gq0vCEjQVYTu9ATk"

chat = ChatMistralAI(api_key=api_key)

messages = [HumanMessage(content="knock knock")]

result = chat.invoke(messages)
print(result)
