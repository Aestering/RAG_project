from llama_index.llms.mistralai import MistralAI

llm = MistralAI(api_key="3GyMujRYXjA3Ti37gq0vCEjQVYTu9ATk")
resp = llm.stream_complete("Paul Graham is ")

for r in resp:
    print(r.delta, end="")