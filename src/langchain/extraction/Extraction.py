from langchain.utils.openai_functions import convert_pydantic_to_openai_function
from src.langchain.pydantic.FunctionModels import Aspects
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain.output_parsers.openai_functions import JsonKeyOutputFunctionsParser
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()
aspect_extraction_func = convert_pydantic_to_openai_function(Aspects)

model_with_func = model.bind(
    functions = [aspect_extraction_func],
    function_call = {"name":"Aspects"}
)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are expert information extractor, Extract the multiple distinct aspect or topic information from the given google review, if not explicitly provided do not guess. return the response as valid json schema."),
    ("user", "{input}")
])

chain = prompt_template | model_with_func | JsonOutputFunctionsParser()
chain_with_topics_only = prompt_template | model_with_func | JsonKeyOutputFunctionsParser(key_name = "aspects")

google_review = """Not bad, definitely above average, but I’m not rushing back. The best thing I got was the bread that came with the Channa Masala. It was super light, buttery, kind of sweet and the bottom was crispy which provided it a great bit of texture. The Masala itself was good but it tasted exactly like the Hyderabad Baingan ka Bartha. I will say, both dishes were packed with flavor, it just happened to be the same one.
The dosa is impressively large, but is a useless vessel for the dips it comes with. 80% of it is too thin and crispy, think the burnt end of a pancake, to actually carry or complement the dips. It is fun to eat through because it is so large and the bottom is a bit thicker so it can pick up some sauce, but other than that, it’s unremarkable.
The Gualb Jamun for dessert tasted like a soggy donut hole. It was fine but I would it order it again.
While Annapurna Cuisine is serving up very authentic Indian food, it isn’t close tot he best I’ve had."""

google_review_2 = """High quality clean vegetaría Indian food. Some of the best chai and chole bhatura in SoCal, hands down

They usually run out of chai everyday 1-2 hours before they close. So get it quick lol

The bhindi is ok but literally everything else is OUTSTANDING. Chole bhatura are my go to, and it ALWAYS hits the spot

Paneer and masala dosas are solid, can’t go wrong

Rasmalai usually great

Service is good but because they’re always so slammed, opportunity for improvement

One of the best vegetarian South Indian restaurants in LA!"""


print(chain_with_topics_only.invoke({"input":google_review}))
print(chain_with_topics_only.invoke({"input":google_review_2}))