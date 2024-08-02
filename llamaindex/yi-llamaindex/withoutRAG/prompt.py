import os
os.environ["YI_API_KEY"] = "dc2935e111024862885468d5cbe358af"

from llama_index.llms.yi import Yi

llm = Yi(model="yi-large")
response = llm.complete("What did the author do growing up?")
print(response)