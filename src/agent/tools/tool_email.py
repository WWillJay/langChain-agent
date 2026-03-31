from langchain.agents import create_agent
from langchain_core.tools import tool

# 你的 LLM 初始化（保持不变）
from langchain_openai import ChatOpenAI

llm_openai = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)


# 带规范 docstring 的工具函数
@tool
def email_send(to: str, subject: str, body: str) -> str:
    """
    发送电子邮件的工具函数

    Args:
        to: 收件人邮箱地址（例如：user@example.com）
        subject: 邮件主题
        body: 邮件正文内容

    Returns:
        str: 邮件发送结果提示
    """
    email = {
        "to": to,
        "subject": subject,
        "body": body
    }
    return f"邮件已发送至{to}"


