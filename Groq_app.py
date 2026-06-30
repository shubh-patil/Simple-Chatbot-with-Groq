import os
import streamlit as st

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage


groq_api_key = st.secrets["GROQ_API_KEY"]
os.environ["LANGCHAIN_API_KEY"] = st.secrets["LANGCHAIN_API_KEY"]
os.environ["LANGCHAIN_PROJECT"] = st.secrets["LANGCHAIN_PROJECT"]
os.environ["LANGCHAIN_TRACING_V2"] = 'true'

st.title("🏋️ Fitness Query Resolver")

query = st.text_input("Ask your fitness related questions")

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=groq_api_key
)

if st.button("Get Response"):

    if not query.strip():
        st.warning("Please enter a question")
    else:
        messages = [
            SystemMessage(content="You are a certified fitness coach specializing in fat loss, muscle gain, and Indian diet plans."),
            HumanMessage(content=query)
        ]

        

        response = ""

        for chunk in model.stream(messages):
            response += chunk.content

        st.write(response)

