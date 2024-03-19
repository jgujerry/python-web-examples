import openai
import streamlit as st


st.title("Stream OpenAI Chat App")
openai.api_key = st.secrets["openai_api_key"]

MODEL_NAME = "gpt-3.5-turbo"


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input():
    st.session_state.messages.append({
        "role": "user",
        "content": prompt,
    })
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        completions = openai.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": m["role"], "content": m["content"]
                }
                for m in st.session_state.messages
            ],
            stream=True
        )
        for response in completions:
            content = response.choices[0].delta.content or ""
            full_response += content
            message_placeholder.markdown(full_response)
        
        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({
        "role": "assistant", "content": full_response
    })
