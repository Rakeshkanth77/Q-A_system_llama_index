from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
import llama_index
import os
from dotenv import load_dotenv


load_dotenv()

def main(url: str)-> None:
    documents = SimpleDirectoryReader(url).load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine =index.as_query_engine()
    response = query_engine.query("what is genai and it benefits")
    print(response)
    
if __name__ == "__main__":
    main(url = r"C:\Users\bepec\Documents\Github_repos_rakeskanth77\Q-A_system_llama_index\data")