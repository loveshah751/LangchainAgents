import openai
import os
from dotenv import load_dotenv


class LLMRunner:

    # define your OPENAI key in .env file
    def __init__(self):
        load_dotenv()
        os.environ["TOKENIZERS_PARALLELISM"] = "false"
        self.api_key = os.getenv("OPENAI_API_KEY")

    # different value for function_call "auto", "none", exact function as lambda like {"name": "get_current_weather"}
    def call_llm(self, messages, functions, function_call_type: str = "auto"):
        openai.api_key = self.api_key
        return openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=messages,
            functions=functions,
            function_call = function_call_type
        )


    def extract_messages(self, messages, functions, function_call_type: str = "auto"):
        return self.call_llm(messages, functions, function_call_type)["choices"][0]["message"]