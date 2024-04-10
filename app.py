from flask import Flask, request, jsonify
from googletrans import Translator, LANGUAGES
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
translator = Translator()

@app.route('/translate', methods=['GET'])
def translate_text_get():
    # This is your existing GET endpoint
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

@app.route('/translate', methods=['POST'])
def translate_text_post():
    data = request.get_json()
    texts = data.get('texts', [])
    dest_language = data.get('lang', '')

    if not texts or not dest_language:
        return jsonify({"error": "Missing texts or language code"}), 400
    
    translations = []
    
    try:
        for text in texts:
            translation = translator.translate(text, dest=dest_language)
            translations.append({
                "original_text": text,
                "translated_text": translation.text
            })
        
        return jsonify({
            "translations": translations,
            "destination_language": LANGUAGES.get(dest_language, "the selected language")
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

