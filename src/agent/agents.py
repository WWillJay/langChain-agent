from langchain.agents import create_agent

from agent.llms import llm_openai, llm_deepseek
from agent.tools.tool_email import email_send
from agent.tools.tool_web import web_search

agent_web = create_agent(
    llm_openai,
    tools=[web_search],
    system_prompt="你是个网页搜索助手，请始终使用web_search工具完成查询任务"
)

agent_email = create_agent(
    llm_deepseek,
    tools=[email_send],
    system_prompt="你是个邮件助手，请始终使用send_email工具完成邮件发送任务"
)

agent_all = create_agent(
    llm_deepseek,
    tools=[web_search, email_send],
    system_prompt="你是有很多功能，请根据需求调用相应的工具"
)