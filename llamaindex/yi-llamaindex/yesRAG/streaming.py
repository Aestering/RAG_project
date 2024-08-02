from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Importing the YI Model
from llama_index.llms.yi import Yi
import os
os.environ["YI_API_KEY"] = "dc2935e111024862885468d5cbe358af"

# Initialise reading data from a source
documents = SimpleDirectoryReader("data").load_data()

# bge-base embedding model
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# Setting Yi as the LLM
Settings.llm = Yi(model="yi-large", request_timeout=360.0)

# Set index process
index = VectorStoreIndex.from_documents(documents)
# storing the index
index.storage_context.persist()

# difference response modes:
# refine, compact, tree_summarize, simple_summarize, no_text, accumulate
query_engine = index.as_query_engine(streaming=True)
response = query_engine.query("What did the author do growing up?")
response.print_response_stream()
