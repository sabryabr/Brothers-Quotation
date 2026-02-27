import streamlit as st
import streamlit.components.v1 as components

# Page Config
st.set_page_config(page_title="Brothers EGY | Quotation", layout="wide")

# This reads the separate HTML file
try:
    with open("quote_system.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # This displays it on the screen
    components.html(html_code, height=1500, scrolling=True)
except FileNotFoundError:
    st.error("Error: 'quote_system.html' not found in the repository!")
