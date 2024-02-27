from dotenv import load_dotenv
import os
import openai
import streamlit as st

# Load environment variables
load_dotenv()

# Initialize OpenAI client with dotenv
client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
)

# Your chatbot logic here
