from flask import Flask, render_template

# Importez la fonction chat_completion depuis le fichier openai.py
from services.openai import chat_completion

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/test_openai")
def test_openai():
    # Appelez la fonction chat_completion et affichez le résultat dans la réponse de la requête
    return str(chat_completion)