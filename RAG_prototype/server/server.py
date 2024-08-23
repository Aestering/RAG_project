from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
import deepl

os.environ["YI_API_KEY"] = "dc2935e111024862885468d5cbe358af"

app = Flask(__name__)
CORS(app)

global index

def create_llama_index():
    try:
        index_dir = "index"
        os.makedirs(index_dir, exist_ok=True)

        from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings

        from llama_index.embeddings.huggingface import HuggingFaceEmbedding 
        Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

        documents = SimpleDirectoryReader("uploads").load_data()
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=index_dir)

        if not os.path.exists(index_dir) or not os.listdir(index_dir):
            return "Error: in indexing document", 400
        
        return jsonify({"message": "File indexed successfully"})
    except Exception as e:
        return f"An error occurred: {e}", 400

def query_index():
    # retrieve the api key
    try:
        import os # REALLY IMPORTANT --> FUNCTION TO IMPORT THE API TO ACCESS LLM
        from llama_index.core import StorageContext, load_index_from_storage
        from llama_index.core.settings import Settings

        # Alternative model
        # from llama_index.llms.dashscope import DashScope
        # Settings.llm = DashScope(model="qwen-max", request_timeout=360.0)

        from llama_index.llms.yi import Yi
        Settings.llm = Yi(model="yi-large", max_tokens=5000)

        index_dir = "index"

        if not os.path.exists(index_dir) or not os.listdir(index_dir):
            return jsonify({"error": f"Index directory '{index_dir}' does not exist or is empty."})
        
        data = request.get_json()
        prompt = data.get("prompt")

        storage_context = StorageContext.from_defaults(persist_dir=index_dir)

        global index
        index = load_index_from_storage(storage_context)
        query_engine = index.as_query_engine()
        response_node = query_engine.query(prompt)
        return jsonify({ "answer": response_node.response})

    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"})

@app.route('/ask_llm', methods=['POST'])
def query_endpoint():
    response = query_index()
    return response
    # return response

@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/upload_file", methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        upload_dir = 'uploads'  # Specify the directory where you want to save uploaded files
        os.makedirs(upload_dir, exist_ok=True)

        file.save(os.path.join(upload_dir, file.filename))

        return create_llama_index()

@app.route('/translate', methods=['POST'])
def translate():
    auth_key = "037dbd64-30f9-4fdf-b75c-8bb546536181:fx"
    translator = deepl.Translator(auth_key)

    text = request.json['text']
    source_lang = request.json['source_lang']
    target_lang = request.json['target_lang']

    try:
        result = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)
        translated_text = result.text
        return jsonify({'translated_text': translated_text})
    except deepl.DeepLException as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run()