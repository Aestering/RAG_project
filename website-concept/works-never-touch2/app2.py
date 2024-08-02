from flask import Flask, request, render_template

import deepl

app = Flask(__name__)

# Set up the DeepL API

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        auth_key = "037dbd64-30f9-4fdf-b75c-8bb546536181:fx"
        translator = deepl.Translator(auth_key)

        text = request.form['text']
        source_lang = request.form['source_lang']
        target_lang = request.form['target_lang']

        try:
            result = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)
            translated_text = result.text
            return render_template('demo2.1.html', translated_text=translated_text)
        except deepl.DeepLException as e:
            return f"Error translating text: {e}", 500
    else:
        return render_template('demo2.1.html')

if __name__ == '__main__':
    app.run(debug=True)