from langchain_core.output_parsers import StrOutputParser 

# Thired party integration using langchain_community 
from langchain_community.llms import Ollama

#llm model
def get_llm_model():
    return Ollama(model="LLAMA2")

def get_output_parser():
    return StrOutputParser()

