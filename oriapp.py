from flask import Flask, request, jsonify
from googletrans import Translator, LANGUAGES

app = Flask(__name__)

translator = Translator()

@app.route('/translate', methods=['GET'])
def translate_text():
    text = request.args.get('text', '')
    dest_language = request.args.get('lang', '')

    if not text or not dest_language:
        return jsonify({"error": "Missing text or language code"}), 400

    try:
        translation = translator.translate(text, dest=dest_language)
        language_name = LANGUAGES.get(dest_language, "the selected language")
        return jsonify({
            "original_text": text,
            "translated_text": translation.text,
            "destination_language": language_name
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

