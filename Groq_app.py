import os
import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

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

        response = model.invoke(messages)

        st.write(response.content)