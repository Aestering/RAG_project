from llama_index.llms.mistralai import MistralAI

llm = MistralAI(api_key="3GyMujRYXjA3Ti37gq0vCEjQVYTu9ATk")

resp = llm.complete("Paul Graham is ")
print(resp)