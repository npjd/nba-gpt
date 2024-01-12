import streamlit as st
from agent import Agent


agent = Agent(verbose=True)

st.write("""
# NBA-GPT
## An open-source alternative to statmuse
""")

st.write("Data only goes back to 1997 — to December 2023")
st.write("No awards or all-star games as well")

input = st.text_input("Ask a question about the NBA", key="input")

if input:
    st.write(agent.invoke(input))

    
