from llama_index.llms.llama_api import LlamaAPI

api_key = "LL-WdNfTVjFcJO83a6K5gdLGTKsUpUZi3chAoZcarQILe60gj1EiuHRU7oRkynIR227"

llm = LlamaAPI(api_key=api_key)

response = llm.complete("Paul Graham is ")
print(response)