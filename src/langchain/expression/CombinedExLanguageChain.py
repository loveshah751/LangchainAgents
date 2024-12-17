from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableMap
from dotenv import load_dotenv

import warnings
warnings.filterwarnings('ignore')

load_dotenv()
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
model = ChatOpenAI(model="gpt-4o-mini")
output_parser = StrOutputParser()

vectorstore = DocArrayInMemorySearch.from_texts(
    ["harrison worked at kensho", "bears like to eat honey"],
    embedding=OpenAIEmbeddings()
)

retriever = vectorstore.as_retriever()

runnable_map = RunnableMap({
    "context": lambda x: retriever.get_relevant_documents(x["question"]),
    "question": lambda x: x["question"],
})

print(runnable_map.invoke({"question": "where did harrison work?"}))

complex_chain = runnable_map| prompt | model | output_parser

print(complex_chain.invoke({"question": "where did harrison work?"}))