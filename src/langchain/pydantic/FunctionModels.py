from enum import Enum
from pydantic import BaseModel, Field


class UnitType(str, Enum):
    C = "celsius",
    F = "fahrenheit"

class get_current_weather(BaseModel):
    """Get the current Weather information"""
    location:str = Field(description="The city and state, e.g. San Francisco, CA")
    unit:UnitType = Field(default=UnitType.C)


class weather_search(BaseModel):
    """Search for weather given an airport code"""
    airport_code:str = Field(description="The airport code to get the Weather for", strict=True)