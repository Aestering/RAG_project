from flask import Flask, request, jsonify, render_template
from llama_index.llms.mistralai import MistralAI

app = Flask(__name__)

llm = MistralAI(api_key="3GyMujRYXjA3Ti37gq0vCEjQVYTu9ATk")

@app.route('/', methods=['GET'])
def index():
    return render_template('lol.html')

@app.route('/generate', methods=['POST'])
async def generate_text():
    prompt = request.json['prompt']
    response = await llm.acomplete(prompt)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)