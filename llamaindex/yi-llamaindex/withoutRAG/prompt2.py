import os
os.environ["YI_API_KEY"] = "dc2935e111024862885468d5cbe358af"

from llama_index.llms.yi import Yi
from llama_index.core.llms import ChatMessage

llm = Yi(model="yi-large")

messages = [
    ChatMessage(
        role="system", content="Your are a pirate with a colourful personality"
    ),
    ChatMessage(role="user", content="What is your name"),
]
resp = llm.chat(messages)
print(resp)