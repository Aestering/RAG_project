import os
os.environ["DASHSCOPE_API_KEY"] = "sk-6c57f1fdfa3f44d8bf5617d5c4586f28"

from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage

chatLLM = ChatTongyi(
    streaming=True,
)

res = chatLLM.stream([HumanMessage(content="hi")], streaming=True)
for r in res:
    print("chat resp:", r)
