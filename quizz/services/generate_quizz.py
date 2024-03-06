import os
from openai import OpenAI

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def generate_quiz(subject):
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)

        prompt = f"Générer un quiz sur le sujet : {subject}. Avec 4 questions, chacune suivie de 4 réponses possibles."

        messages = [
            {"role": "system", "content": "You are a quiz generator, and you are creating a quiz on a specific given subject."},
            {"role": "user", "content": prompt}
        ]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )

        quiz = response.choices[0].message.content
        return quiz
    except Exception as e:
        print(f"Error: {str(e)}")
        return None