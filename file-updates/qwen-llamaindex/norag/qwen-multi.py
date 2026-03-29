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

# 1st round
resp = dashscope_llm.chat(messages)
print(resp)

# add response to messages
messages.append(
    ChatMessage(role=MessageRole.ASSISTANT, content=resp.message.content)
)

messages.append(
    ChatMessage(role=MessageRole.USER, content="How to make it without sugar")
)

# Second round
resp = dashscope_llm.chat(messages)
print(resp)
