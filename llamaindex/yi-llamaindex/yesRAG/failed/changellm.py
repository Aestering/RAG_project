import os
os.environ["YI_API_KEY"] = "dc2935e111024862885468d5cbe358af"

from llama_index.core import KeywordTableIndex, SimpleDirectoryReader
from llama_index.llms.yi import Yi

documents = SimpleDirectoryReader("data").load_data()

# define LLM
llm = Yi(model="yi-large")

# build index
index = KeywordTableIndex.from_documents(documents, llm = llm)

# get response from query
query_engine = index.as_query_engine()
response = query_engine.query("Who is Paul Graham?")
for r in response:
    print(r.delta, end="")
