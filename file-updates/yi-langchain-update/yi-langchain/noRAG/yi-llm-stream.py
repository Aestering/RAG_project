import os
os.environ["YI_API_KEY"] = "dc2935e111024862885468d5cbe358af"

from langchain_community.llms.yi import YiLLM

# Load the model
llm = YiLLM(model="yi-large", region = "international")

for chunk in llm.stream("Describe the key features of the Yi language model series."):
    print(chunk, end="", flush=True)