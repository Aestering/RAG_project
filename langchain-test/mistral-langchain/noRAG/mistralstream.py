from langchain_core.messages import HumanMessage
from langchain_mistralai.chat_models import ChatMistralAI
api_key="###"

chat = ChatMistralAI(api_key=api_key)

messages = [HumanMessage(content="knock knock")]

chat.invoke(messages)

for chunk in chat.stream(messages):
    print(chunk.content, end="")
