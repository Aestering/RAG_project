import os
os.environ["YI_API_KEY"] = "###"

from llama_index.llms.yi import Yi

llm = Yi(model="yi-large")
response = llm.stream_complete("Who is Paul Graham?")
for r in response:
    print(r.delta, end="")
