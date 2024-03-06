from flask import Flask, render_template, jsonify
from services.generate_quizz import generate_quiz
from services.openai import chat_completion
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/test_openai")
def test_openai():
    return str(chat_completion)

@app.route("/generate_quiz", methods=['GET'])
def handle_generate_quiz():
    try:
        subject = "capitales"
        quiz = generate_quiz(subject)
        if quiz:
            return jsonify({"quiz": quiz})
        else:
            return jsonify({"error": "Failed to generate quiz."})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
