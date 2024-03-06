from flask import Flask, render_template
from services.openai import chat_completion

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/test_openai")
def test_openai():
    # Appelez la fonction chat_completion
    # Affichez le résultat dans la réponse de la requête
    return str(chat_completion)
