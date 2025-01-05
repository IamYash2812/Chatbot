from langchain_core.prompts import ChatPromptTemplate

def get_chat_prompt():
    prompt = ChatPromptTemplate([
    ("system","your personalized assitant. Please respond to user requests"),
    ("user","Questions:{question}")])
    return prompt
    