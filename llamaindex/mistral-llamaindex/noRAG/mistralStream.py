from llama_index.llms.mistralai import MistralAI

llm = MistralAI(api_key="###")
resp = llm.stream_complete("Paul Graham is ")

for r in resp:
    print(r.delta, end="")
