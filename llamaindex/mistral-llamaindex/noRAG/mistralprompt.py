from llama_index.llms.mistralai import MistralAI

llm = MistralAI(api_key="###")

resp = llm.complete("Paul Graham is ")
print(resp)
