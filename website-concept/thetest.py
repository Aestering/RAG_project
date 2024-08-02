import deepl

auth_key = "037dbd64-30f9-4fdf-b75c-8bb546536181:fx"
translator = deepl.Translator(auth_key)

result = translator.translate_text("Hello, world!", targßet_lang="FR")
print(result.text)