from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
prompt = ChatPromptTemplate.from_template(
    "Tell me a joke about {topic}.",
)
model = ChatOpenAI(model="gpt-4o-mini")
output_parser = StrOutputParser()

chain = prompt | model | output_parser


print(chain.invoke({"topic": "chickens"}))