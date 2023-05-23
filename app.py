from flask import Flask, render_template, request
import googletrans
import textblob

app = Flask(__name__)

languages = googletrans.LANGUAGES
language_list = list(languages.values())

import random

@app.route('/')
@app.route('/index.html')
def home():
    random_languages = random.sample(language_list, 50)
    return render_template('index.html', language_list=language_list, random_languages=random_languages)
@app.route('/aboutus.html')
def aboutus():
    return render_template('aboutus.html')


@app.route('/translate', methods=['POST'])
def translate():
    original_text = request.form['original_text']
    from_language = request.form['from_language']
    to_language = request.form['to_language']

    try:
        from_language_key = next(key for key, value in languages.items() if value == from_language)
        to_language_key = next(key for key, value in languages.items() if value == to_language)

        words = textblob.TextBlob(original_text)
        translated_text = words.translate(from_lang=from_language_key, to=to_language_key)

        return render_template('index.html', language_list=language_list, translated_text=translated_text)

    except Exception as e:
        error_message = str(e)
        return render_template('index.html', language_list=language_list, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
