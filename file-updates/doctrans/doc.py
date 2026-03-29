import deepl
import os

os.environ["DEEPL_AUTH_KEY"] = "#######"

translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))

input_path = "/Users/aester/website-concept/doctrans/IO/JP Toppan_Q&AResultsBriefing_2024_Test for RAG.pdf"
output_path = "/Users/aester/website-concept/doctrans/IO/JP test translation.pdf"

try:
    # Upload and translate a document
    translator.translate_document_from_filepath(
        input_path,
        output_path,
        target_lang="EN-GB"
    )

    #with open(input_path, "rb") as in_file, open(output_path, "wb") as out_file:
        #translator.translate_document(
            #in_file,
            #out_file,
            #target_lang="EN-GB",
            #formality="more"
        #)

except deepl.DocumentTranslationException as error:
    doc_id = error.document_handle.id
    doc_key = error.document_handle.key
    print(f"Error after uploading ${error}, id: ${doc_id} key: ${doc_key}")
except deepl.DeepLException as error:
    print(error)
