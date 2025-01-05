
import streamlit as st
from llm_config import get_llm_model
from llm_config import get_output_parser
from promt_info import get_chat_prompt_info

#get LLAMA2 model
llm = get_llm_model()

#get prompt_template
prompt_template = get_chat_prompt_info()

#get ouput parser
output_parser = get_output_parser()

chain = prompt_template|llm|output_parser

#streamlit framework
st.title("langchain Demo with ollama")
input_text =st.text_input("Ask anything...")


if input_text:
    st.write(chain.invoke({"question":input_text}))
    