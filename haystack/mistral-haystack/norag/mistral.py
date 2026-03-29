import os
from haystack.dataclasses import ChatMessage
from haystack_integrations.components.generators.mistral import MistralChatGenerator

os.environ["MISTRAL_API_KEY"] = "###"
model = "mistral-medium"

client = MistralChatGenerator(model=model)

response = client.run(
    messages=[ChatMessage.from_user("What is the best French cheese?")]
)
print(response)
