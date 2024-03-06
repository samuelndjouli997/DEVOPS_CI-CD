import os
from dotenv import load_dotenv
import unittest
from unittest.mock import patch
from services.openai import OpenAI

load_dotenv()


def generate_chat_completion():
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "You are a helpful assistant."},
        ],
    )
    return chat_completion.choices[0]['message']['content']


class TestGenerateChatCompletion(unittest.TestCase):

    @patch('openai.OpenAI')
    def test_generate_chat_completion(self, mock_openai):
        mock_client = mock_openai.return_value
        mock_client.chat.completions.create.return_value = {
            "choices": [
                {
                    "message": {
                        "content": "That's great to hear!"
                        "I'm here to help you with anything you need."
                    }
                }
            ]
        }

        result = generate_chat_completion()
        self.assertEqual(
            result,
            "That's great to hear!"
            "I'm here to help you with anything you need."
            )


if __name__ == '__main__':
    unittest.main()
