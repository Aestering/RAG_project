import openai
from openai import OpenAI
API_BASE = "https://api.01.ai/v1"
API_KEY = "dc2935e111024862885468d5cbe358af"
client = OpenAI(
    api_key=API_KEY,
    base_url=API_BASE
)
completion = client.chat.completions.create(
    model="yi-large",
    messages=[{"role": "user", "content": "Hi, who are you?"}]
)
print(completion)






