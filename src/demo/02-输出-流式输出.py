# 流式输出
from agent.llms import llm_deepseek

for chunk in llm_deepseek.stream('简单三句话描述langchain作用'):
    print(chunk.content, end="", flush=True)