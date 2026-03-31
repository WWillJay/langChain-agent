import os

from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain_openai import ChatOpenAI

# 加载环境变量
load_dotenv(override=True)

# OpenAI
llm_openai = ChatOpenAI(
    model_name=os.getenv('OPENAI_MODEL'),
    temperature=0.5,
    api_key=os.getenv('OPENAI_API_KEY'),
    base_url=os.getenv('OPENAI_API_BASE')
)

# DeepSeek
llm_deepseek = ChatDeepSeek(
    model_name=os.getenv('DEEPSEEK_MODEL'),
    temperature=0.5,
    api_key=os.getenv('DEEPSEEK_API_KEY'),
    api_base=os.getenv('DEEPSEEK_API_BASE')
)
