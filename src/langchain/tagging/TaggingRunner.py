from langchain.utils.openai_functions import convert_pydantic_to_openai_function
from src.langchain.pydantic.FunctionModels import Tagging
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser

from dotenv import load_dotenv
import warnings

warnings.filterwarnings('ignore')
load_dotenv()

tagging_function = convert_pydantic_to_openai_function(Tagging)
model = ChatOpenAI(temperature=0)

model_with_function = model.bind(
    functions = [tagging_function],
    function_call = {"name":"Tagging"}
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Think carefully, and then tag the text as instructed"),
        ("user", "{input}")
    ]
)

chain = prompt | model_with_function | JsonOutputFunctionsParser()
google_review = """Not bad, definitely above average, but I’m not rushing back. The best thing I got was the bread that came with the Channa Masala. It was super light, buttery, kind of sweet and the bottom was crispy which provided it a great bit of texture. The Masala itself was good but it tasted exactly like the Hyderabad Baingan ka Bartha. I will say, both dishes were packed with flavor, it just happened to be the same one.
The dosa is impressively large, but is a useless vessel for the dips it comes with. 80% of it is too thin and crispy, think the burnt end of a pancake, to actually carry or complement the dips. It is fun to eat through because it is so large and the bottom is a bit thicker so it can pick up some sauce, but other than that, it’s unremarkable.
The Gualb Jamun for dessert tasted like a soggy donut hole. It was fine but I would it order it again.
While Annapurna Cuisine is serving up very authentic Indian food, it isn’t close tot he best I’ve had."""
#print(chain.invoke({"input": "ਮੈਨੂੰ ਖਾਣਾ ਪਸੰਦ ਨਹੀਂ ਹੈ"}))
print(chain.invoke({"input": google_review}))


