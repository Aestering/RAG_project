# Copyright 2023 DeepL SE (https://www.deepl.com)
# Use of this source code is governed by an MIT
# license that can be found in the LICENSE file.

import sys
import io
import deepl
import os

env_auth_key = "DEEPL_AUTH_KEY"
env_server_url = "DEEPL_SERVER_URL"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        auth_key = os.getenv(env_auth_key)
        server_url = os.getenv(env_server_url)
        if auth_key is None:
            return "Please provide authentication key via the DEEPL_AUTH_KEY environment variable", 500

        translator = deepl.Translator(auth_key, server_url=server_url)
        text = request.form['text']
        source_lang = request.form['source_lang']
        target_lang = request.form['target_lang']

        try:
            result = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)
            translated_text = result.text
            return render_template('website.html', translated_text=translated_text)
        except deepl.DeepLException as e:
            return f"Error translating text: {e}", 500
    else:
        return render_template('website.html')

if __name__ == '__main__':
    app.run(debug=True)