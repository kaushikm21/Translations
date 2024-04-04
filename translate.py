from googletrans import Translator, LANGUAGES

def translate_text(text, dest_language):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text

# Taking input from the user
english_text = input("Enter the English text to translate: ")
print("Enter the destination language code:")
print("de for German, pt for Portuguese, es for Spanish, it for Italian, tl for Filipino, fr for French, ja for Japanese, th for Thai, fi for Finnish")
dest_language = input("Language code: ")

translated_text = translate_text(english_text, dest_language)
language_name = LANGUAGES.get(dest_language, "the selected language")
print(f"Translated to {language_name}: {translated_text}")
