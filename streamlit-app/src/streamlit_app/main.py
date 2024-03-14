from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="Streamlit Example",
    page_icon="👋"
)

st.sidebar.success("Choose an example above.")

st.write("# Hello there 👋, welcome to Streamlit app!")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    """
)
