from llama_index.core.llms import ChatMessage
from llama_index.llms.mistralai import MistralAI



messages = [
    ChatMessage(role = "system", content = "You are CEO of MistralAI."),
    ChatMessage(role = "user", content = "Tell me the story about La plateforme"),
]
resp = MistralAI(api_key="3GyMujRYXjA3Ti37gq0vCEjQVYTu9ATk").chat(messages)
print(resp)