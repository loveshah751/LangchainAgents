from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch
from dotenv import load_dotenv

load_dotenv()
#make sure to give access to text-embedding-ada-002 model in OPENAI Platform for given API Key
vectorstore = DocArrayInMemorySearch.from_texts(
    ["harrison worked at kensho", "bears like to eat honey"],
    embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever()

print(retriever.get_relevant_documents("where did harrison work?"))