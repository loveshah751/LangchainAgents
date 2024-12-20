from enum import Enum
from pydantic import BaseModel, Field
from typing import List

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


class Tagging(BaseModel):
     """"Tag the piece of text with particular info."""
     sentiment:str = Field(description="sentiment of text, should be `positive`, `negative`, or `neutral`")
     language:str = Field(description="language of text")

class Aspect(BaseModel):
        """Aspect / topics for the piece of text."""
        topic:str = Field(description="aspect of the text, should be particular topic what text is all about")
        text:str = Field(description="original text which as provide as input")

class Aspects(BaseModel):
      """Collection of topic information"""
      aspects:List[Aspect] = Field(description= "List of topics extracted from the input text")

