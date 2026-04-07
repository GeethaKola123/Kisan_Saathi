from deep_translator import GoogleTranslator

def translate_text(text, target_lang):
    lang_map = {"English": "en", "Hindi": "hi", "Telugu": "te"}
    return GoogleTranslator(source="auto", target=lang_map[target_lang]).translate(text)
