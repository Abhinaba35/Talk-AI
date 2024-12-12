import streamlit as st 
from openai import OpenAI 
  
st.title("Talk AI") 
  
if "messages" not in st.session_state: 
  st.session_state.messages = [] 
  
for message in st.session_state.messages: 
  with st.chat_message(message["role"]): 
    st.markdown(message["content"]) 
  
client = OpenAI(base_url="http://localhost:11434/v1", api_key="random-text") 
 
prompt = st.chat_input("What's up?") 
  
  
if prompt: 
  with st.chat_message("user"): 
    st.markdown(prompt) 
  
  st.session_state.messages.append({"role":"user","content":prompt}) 
  
  
  with st.chat_message("assistant"): 
    stream = client.chat.completions.create( 
      model = "llama3", 
 
 
 
      messages = [ 
        {"role": message["role"], "content": message["content"]} 
        for message in st.session_state.messages 
      ], 
      stream=True 
    ) 
    response = st.write_stream(stream) 
  
  st.session_state.messages.append({"role":"assistant","content":response}) 