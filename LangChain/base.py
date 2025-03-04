from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
import os

def init():
    load_dotenv()
    llm = ChatDeepSeek(
        model="deepseek-reasoner",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=os.getenv("DEEP_SEEK_API_KEY"),
        # other params...
    )
    return llm