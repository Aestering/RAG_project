import os
os.environ["DASHSCOPE_API_KEY"] = "####"

from llama_index.llms.dashscope import DashScope, DashScopeGenerationModels
from llama_index.core.base.llms.types import MessageRole, ChatMessage

dashscope_llm = DashScope(model_name=DashScopeGenerationModels.QWEN_MAX)

messages = [
    ChatMessage(
        role=MessageRole.SYSTEM, content="You are a helpful assistant."
    ),
    ChatMessage(role=MessageRole.USER, content="How to make cake?"),
]

#resp = dashscope_llm.chat(messages)
#print(resp)

responses = dashscope_llm.stream_chat(messages)
for response in responses:
    print(response.delta, end='')
