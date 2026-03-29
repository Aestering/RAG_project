from flask import Flask, render_template, request, redirect, url_for, send_file
import os
from deepl import Translator, DocumentTranslationException, DeepLException

app = Flask(__name__)

os.environ["DEEPL_AUTH_KEY"] = "########"

@app.route('/')
def index():
    return render_template('doc.html')

@app.route('/translate_upload', methods=['POST'])
def translate_document_upload():
    file = request.files.get('file')
    target_lang = request.form.get('target_lang')
    if file and target_lang:
        # Get the absolute file path
        upload_folder = os.path.join(app.root_path, 'uploads')
        os.makedirs(upload_folder, exist_ok=True)
        input_path = os.path.abspath(os.path.join(upload_folder, file.filename))
        file.save(input_path)

        # Store the input path and target language in the session
        session['input_path'] = input_path
        session['target_lang'] = target_lang

        return redirect(url_for('translate_document_get_status'))
    return redirect(url_for('index'))

@app.route('/translate_status')
def translate_document_get_status():
    input_path = session.get('input_path')
    target_lang = session.get('target_lang')
    if input_path and target_lang:
        # Your translation logic goes here
        translator = Translator(os.environ['DEEPL_AUTH_KEY'])
        output_path = os.path.join(os.path.dirname(input_path), 'translated_' + os.path.basename(input_path))

        try:
            translator.translate_document_from_filepath(
                input_path,
                output_path,
                target_lang
            )
            return redirect(url_for('translate_document_download', output_path=output_path))
        except DocumentTranslationException as error:
            doc_id = error.document_handle.id
            doc_key = error.document_handle.key
            return f"Error after uploading {error}, id: {doc_id} key: {doc_key}", 500
        except DeepLException as error:
            return str(error), 500
        finally:
            if os.path.exists(input_path):
                os.remove(input_path)
    return redirect(url_for('index'))

@app.route('/translate_download')
def translate_document_download():
    output_path = request.args.get('output_path')
    if output_path and os.path.exists(output_path):
        return send_file(output_path, as_attachment=True)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
