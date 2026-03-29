from llama_index.llms.llama_api import LlamaAPI

api_key = "###"

llm = LlamaAPI(api_key=api_key)

response = llm.complete("Paul Graham is ")
print(response)
