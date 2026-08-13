from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

MODEL_NAME = "llama-3.3-70b-versatile"

llm = ChatGroq(
    model=MODEL_NAME,
    api_key=os.getenv("GROQ_API_KEY")
)