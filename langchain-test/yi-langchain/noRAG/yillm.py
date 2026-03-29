import os
os.environ["YI_API_KEY"] = "###"

from langchain_community.llms import yi
from langchain_ol

# Basic usage
res = llm.invoke("What is your name?")
print(res)
