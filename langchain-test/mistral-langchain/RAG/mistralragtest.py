import os
os.environ["MISTAL_API_KEY"] = "###"

from langchain_mistralai import ChatMistralAI

llm = ChatMistralAI(model="mistral-large-latest")

from langchain import hub
prompt = hub.pull("rlm/rag-prompt")

example_messages = prompt.invoke(
    {"context": "The sun dipped below the horizon, casting a warm, golden glow over the peaceful meadow. A gentle breeze rustled the tall grass, and the distant chirping of crickets filled the air. In the distance, a lone oak tree stood tall, its branches reaching up towards the slowly fading sky. A sense of tranquility and calm enveloped the scene, as if time had slowed to a peaceful crawl, inviting the weary traveler to pause and savor the moment.", "question": "Can you translate this paragraph into Simplified Chinese"}
).to_messages()



print(example_messages[0].content)
