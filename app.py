import streamlit as st
from agent import Agent


agent = Agent(verbose=True)

st.write("""
# NBA-GPT
An open-source alternative to statmuse
""")

input = st.text_input("Ask a question about the NBA", key="input")

if input:
    st.write(agent.invoke(input))

    
