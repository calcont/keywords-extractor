from flask import Flask, render_template, request
from rake_nltk import Rake
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract_keywords():
    text = request.form['text']
    rake_nltk_var = Rake()
    rake_nltk_var.extract_keywords_from_text(text)
    keyword_extracted = rake_nltk_var.get_ranked_phrases()
    response = json.dumps({'Keyword': keyword_extracted, 'keywordLen': len(
                keyword_extracted)}, default=str)
    
    return {'keywords': response}

if __name__ == '__main__':
    app.run(debug=True)
