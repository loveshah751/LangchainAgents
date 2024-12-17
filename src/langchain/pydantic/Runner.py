from langchain_core.utils.function_calling import convert_python_function_to_openai_function
from src.langchain.pydantic.FunctionModels import get_current_weather, weather_search
from src.langchain.pydantic.User import User, Users

user = User(name = "Lovepreet", age = 29, location = "LA")
user2 = User(name = "ABC", age = 29, location = "LA")

users = Users(users = [user, user2])
print(user)
print(users)

import warnings
warnings.filterwarnings('ignore')

current_weather_func = convert_python_function_to_openai_function(get_current_weather)
weather_search_func = convert_python_function_to_openai_function(weather_search)
print(current_weather_func)
print(weather_search_func)

