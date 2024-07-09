from os import getenv
from dspy import LM
from google.generativeai import GenerativeModel
from dotenv import load_dotenv

load_dotenv()

class GeminiLM(LM):
    def __init__(self, model_name):
        self.model_name = model_name
        self.history = []
        self.model = GenerativeModel(model_name)
        self.provider = "default"

    def _get_choice_text(self, choice):
        return choice["message"]["content"]

    def transform_request_output(self, response):
        # Construct the dictionary

        choice = {
            "message": {
                "role": "assistant",
                "content": response.text
            },
        }
        result = {
            "choices": [
                choice
            ],
        }

        return result

    def basic_request(self, prompt: str, **kwargs):
        response_data = self.model.generate_content(prompt)
        
        final_data = self.transform_request_output(response_data)

        self.history.append({
            "prompt": prompt,
            "response": final_data,
            "kwargs": kwargs,
        })

        return final_data

    def __call__(self, prompt, **kwargs):
        response_data = self.basic_request(prompt)
        completions = [choice["message"]["content"] for choice in response_data["choices"]]
        return completions