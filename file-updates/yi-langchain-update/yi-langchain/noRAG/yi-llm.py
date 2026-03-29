import os
os.environ["YI_API_KEY"] = "###"

from langchain_community.llms.yi import YiLLM

# Load the model
llm = YiLLM(model="yi-large", region = "international")

# basic usage
res = llm.invoke("What's your name?")
print(res)
