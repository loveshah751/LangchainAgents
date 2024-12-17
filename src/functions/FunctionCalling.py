import json
from http.client import responses

from src.common.LLMRunner import LLMRunner
from src.common.WeatherUtils import get_current_weather

functions = [
    {
        "name":"get_current_weather",
        "description":"get Weather information",
        "parameters":{
            "type":"object",
            "properties": {
                "location": {
                    "type":"string",
                    "description":"The city and state, e.g. San Francisco, CA"
                },
                "unit":{
                    "type":"string",
                    "enum": ["celsius", "fahrenheit"]
                }
            }
        }
    }
]

messages = [
    {
        "role": "user",
        "content": "What's the weather like in Boston?"
    }
]

chat_gpt = LLMRunner()

response = chat_gpt.call_llm(messages, functions)
response_message = chat_gpt.extract_messages(messages, functions)
function_argument = json.loads(response_message["function_call"]["arguments"])
observation = get_current_weather(function_argument)

messages.append(
    {
        "role": "function",
        "name": "get_current_weather",
        "content": observation,
    }
)

final_response = chat_gpt.call_llm(messages, functions, "none")
print(final_response)