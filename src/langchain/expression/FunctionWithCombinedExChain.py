from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

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
                "unit": {
                    "type":"string",
                    "enum":["celsius", "fahrenheit"]
                }
            }
        }
    },
    {
        "name": "weather_search",
        "description": "Search for weather given an airport code",
        "parameters": {
            "type": "object",
            "properties": {
                "airport_code": {
                    "type": "string",
                    "description": "The airport code to get the weather for"
                },
            },
            "required": ["airport_code"]
        }
    }
]

prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}")
    ]
)
model = ChatOpenAI()
model.bind(functions = functions)

runnable = prompt | model

print(runnable.invoke({"input": "what is the weather in sf"}))