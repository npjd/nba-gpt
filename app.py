import streamlit as st
from agent import NBAAgent
from search import Search


agent = NBAAgent(verbose=True)
search = Search()

st.write("""
# NBA-GPT
## An open-source alternative to statmuse
""")

st.write("Data only goes back to 1997 — to December 2023")
st.write("No awards or all-star games as well")

input = st.text_input("Ask a question about the NBA", key="input")

if input:
    output = agent.invoke(input)
    youtube_link = search.invoke(output["output"])
    st.write(output)
    st.video(youtube_link)