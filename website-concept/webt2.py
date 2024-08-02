from flask import Flask, render_template, request, jsonify
import deepl
import io
import os

app = Flask(__name__)

env_auth_key = "DEEPL_AUTH_KEY"
env_server_url = "DEEPL_SERVER_URL"


def main() -> None:
    auth_key = os.getenv(env_auth_key)
    server_url = os.getenv(env_server_url)
    if auth_key is None:
        raise Exception(
        f"Please provide authentication key via the {env_auth_key} "
        "environment variable or --auth_key argument"
        )

    # Create a Translator object, and call get_usage() to validate connection
    translator: deepl.Translator = deepl.Translator(
        auth_key, server_url=server_url
    )
    u: deepl.Usage = translator.get_usage()
    u.any_limit_exceeded

# Use most translation features of the library
    _ = translator.translate_text(
        ["I am an example sentence", "I am another sentence"],
        source_lang="EN",
        target_lang="FR",
        formality=deepl.Formality.DEFAULT,
        tag_handling=None,
    )





if __name__ == '__main__':
    app.run(debug=True)