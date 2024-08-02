import os
os.environ["YI_API_KEY"] = "dc2935e111024862885468d5cbe358af"

from langchain_community.llms import yi
from langchain_ol

# Basic usage
res = llm.invoke("What is your name?")
print(res)