import os
os.environ["YI_API_KEY"] = "###"

from langchain_community.chat_models.yi import ChatYi

# Load the model
llm = ChatYi(model="yi-large", 
             region = "international",
             temperature = 0,
             timeout = 60,
             yi_api_base = "https://api.01.ai/v1/chat/completions")


# basic usage
res = llm.invoke("What's your name?")
print(res)
