import os
os.environ["DASHSCOPE_API_KEY"] = "####"

from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, SystemMessage

chatLLM = ChatTongyi(
    streaming=True,
)

messages = [
    SystemMessage(
        content="You are a helpful assistant that translates English to French."
    ),
    HumanMessage(
        content="Translate this sentence from English to French. I love programming"
    ),
]
hey = chatLLM(messages)
print(hey)
