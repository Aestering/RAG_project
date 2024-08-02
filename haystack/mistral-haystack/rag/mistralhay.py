from haystack import Pipeline
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.dataclasses import ChatMessage
from haystack.utils.auth import Secret

from haystack.components.builders import DynamicChatPromptBuilder

# Available files for pushing as documents:
# TextFileToDocument, HTMLToDocument, MarkdownToDocument, PDFMinerToDocument (PDF)/PyPDFToDocument,
# PPTXToDocument, TikaDocumentConverter (files of different types + need tika server)
# More details: docs.haystack.deepset.ai/reference/converters-api
from haystack.components.converters import TextFileToDocument

from haystack.components.preprocessors import DocumentSplitter
from haystack.components.retrievers.in_memory import InMemoryEmbeddingRetriever
from haystack.components.writers import DocumentWriter
from haystack_integrations.components.embedders.mistral import MistralDocumentEmbedder, MistralTextEmbedder
from haystack_integrations.components.generators.mistral import MistralChatGenerator
api_key="3GyMujRYXjA3Ti37gq0vCEjQVYTu9ATk"

document_store = InMemoryDocumentStore()



docs = TextFileToDocument().run(sources=["data/essay.txt"])
split_docs = DocumentSplitter(split_by="passage", split_length=2).run(documents=docs["documents"])
embeddings = MistralDocumentEmbedder(api_key=Secret.from_token(api_key)).run(documents=split_docs["documents"])
DocumentWriter(document_store=document_store).run(documents=embeddings["documents"])


text_embedder = MistralTextEmbedder(api_key=Secret.from_token(api_key))
retriever = InMemoryEmbeddingRetriever(document_store=document_store)
prompt_builder = DynamicChatPromptBuilder(runtime_variables=["documents"])
llm = MistralChatGenerator(api_key=Secret.from_token(api_key), 
                           model='mistral-small')

chat_template = """Answer the following question based on the contents of the documents.\n
                Question: {{query}}\n
                Documents: 
                {% for document in documents %}
                    {{document.content}}
                {% endfor%}
                """
messages = [ChatMessage.from_user(chat_template)]

rag_pipeline = Pipeline()
rag_pipeline.add_component("text_embedder", text_embedder)
rag_pipeline.add_component("retriever", retriever)
rag_pipeline.add_component("prompt_builder", prompt_builder)
rag_pipeline.add_component("llm", llm)


rag_pipeline.connect("text_embedder.embedding", "retriever.query_embedding")
rag_pipeline.connect("retriever.documents", "prompt_builder.documents")
rag_pipeline.connect("prompt_builder.prompt", "llm.messages")

question = "What were the two main things the author worked on before college?"
# question = "What happened in april 1990?"

result = rag_pipeline.run(
    {
        "text_embedder": {"text": question},
        "prompt_builder": {"template_variables": {"query": question}, "prompt_source": messages},
        "llm": {"generation_kwargs": {"max_tokens": 225}},
    }
)

print(result["llm"]["replies"][0].content)