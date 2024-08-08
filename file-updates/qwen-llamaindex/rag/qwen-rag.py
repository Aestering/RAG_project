from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Importing the Dashscope Model
from llama_index.llms.dashscope import DashScope
import os
os.environ["DASHSCOPE_API_KEY"] = "sk-6c57f1fdfa3f44d8bf5617d5c4586f28"

# Initialise reading data from a source
documents = SimpleDirectoryReader("document").load_data()

# bge-base embedding model
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# Setting Yi as the LLM
Settings.llm = DashScope(model="qwen-max", request_timeout=360.0)

# Set index process
index = VectorStoreIndex.from_documents(documents)
# storing the index
index.storage_context.persist()

query_engine = index.as_query_engine()


response = query_engine.query("What did the author do growing up in Chinese?")
print(response)

