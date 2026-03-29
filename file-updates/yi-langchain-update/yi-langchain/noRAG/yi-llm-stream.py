import os
os.environ["YI_API_KEY"] = "###"

from langchain_community.llms.yi import YiLLM

# Load the model
llm = YiLLM(model="yi-large", region = "international")

for chunk in llm.stream("Describe the key features of the Yi language model series."):
    print(chunk, end="", flush=True)
