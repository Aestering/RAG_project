from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext, load_index_from_storage
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Importing the YI Model
from llama_index.llms.yi import Yi
import os
import os.path
os.environ["YI_API_KEY"] = "dc2935e111024862885468d5cbe358af"

# Viewing Queries and Events Using Logging
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Initialise reading data from a source
documents = SimpleDirectoryReader("data").load_data()

# bge-base embedding model
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# Setting Yi as the LLM
Settings.llm = Yi(model="yi-large", request_timeout=360.0)



# Check if storage already exists
PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    # load the documents and create the index
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)


# Can now query the index
query_engine = index.as_query_engine()
response = query_engine.query("Can you translate the first line to Chinese?")
print(response)