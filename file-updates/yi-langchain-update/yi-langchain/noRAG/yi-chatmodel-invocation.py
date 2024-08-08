import os
os.environ["YI_API_KEY"] = "dc2935e111024862885468d5cbe358af"

from langchain_community.chat_models.yi import ChatYi
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatYi(model="yi-large", 
             region = "international",
             temperature = 0,
             timeout = 60,
             yi_api_base = "https://api.01.ai/v1/chat/completions")

messages = [
    SystemMessage(content="You are an AI assistant specializing in technology trends."),
    HumanMessage(
        content="What are the potential applications of large language models in healthcare?"
    ),
]

ai_msg = llm.invoke(messages)
print(ai_msg)