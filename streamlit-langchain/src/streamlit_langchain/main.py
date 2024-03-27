import streamlit as st
from langchain_openai import OpenAI

st.title('🦜🔗 Streamlit Langchain Example App')

openai_api_key = st.secrets["openai_api_key"]


def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))


with st.form('chatform'):
    text = st.text_area('Enter text:', 'What are the key factors to develop a successful web app by using Python?')
    submitted = st.form_submit_button('Submit')
    
    if not openai_api_key.startswith('sk-'):
        st.warning('Please config your OpenAI API key in ~/.streamlit/secrets.toml!', icon='⚠')
    
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
