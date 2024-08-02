from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.mistralai import MistralAI
from llama_index.embeddings.mistralai import MistralAIEmbedding
from llama_index.core.settings import Settings

api_key="3GyMujRYXjA3Ti37gq0vCEjQVYTu9ATk"
documents = SimpleDirectoryReader("data").load_data()

# define llm
llm = MistralAI(api_key=api_key, model="mistral-medium")
embed_model = MistralAIEmbedding(model_name="mistral-embed", api_key=api_key)
Settings.llm = llm
Settings.embed_model = embed_model

# Create vector store index
index = VectorStoreIndex.from_documents(documents)

# Create query engine
query_engine = index.as_query_engine(similarity_top_k = 2)
response = query_engine.query(
    "What were the two main things the author worked on before college outputted in Traditional Chinese?"
)
print(str(response))




