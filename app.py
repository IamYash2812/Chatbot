
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

#chat history
if "chat_history" not in st.seession_state:
    st.seession_state["chat_history"]  = []


#streamlit framework
st.title("langchain Demo with ollama")
input_text =st.text_input("Ask anything...")


if input_text:
    response = chain.invoke({"question":input_text})
    st.session_state['chat_history'].append({"question":input_text,"response":response} )
    st.write(response)

st.write("Chat History")
for entry in st.session_state["chat_history"]:
    st.write(f"You: {entry['question']}")
    st.write(f"VLMBOT: {entry['response']}")
