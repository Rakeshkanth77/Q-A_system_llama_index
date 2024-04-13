from llama_index.llms.openai import OpenAI
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import VectorStoreIndex
import llama_index
import os
from dotenv import load_dotenv


load_dotenv()

def main(url: str)-> None:
    documents = SimpleWebPageReader(html_to_text= True).load_data(urls=[url])
    index = VectorStoreIndex.from_documents(documents)
    query_engine =index.as_query_engine()
    response = query_engine.query("what is genai and it benefits")
    print(response)
    
if __name__ == "__main__":
    main(url = 'https://www.analyticsvidhya.com/blog/2023/04/what-is-generative-ai/')