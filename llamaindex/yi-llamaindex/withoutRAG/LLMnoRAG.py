from llama_index.llms.openai_like import OpenAILike
from llama_index.core.llms import ChatMessage

model = OpenAILike(api_base="https://api.01.ai/v1", api_key = "dc2935e111024862885468d5cbe358af", model="yi-large", is_chat_model=True)

response = model.chat(messages=[ChatMessage(content="Hi, Who are you?")])
print(response)