from agent.llms import llm_openai, llm_deepseek

# OpenAI
response = llm_openai.invoke("简单三句话描述python优点")
print(response)

# DeepSeek
response_deepseek = llm_deepseek.invoke("简单三句话描述langchain作用")
print(response_deepseek)

# 流式输出
for chunk in llm_deepseek.stream('简单三句话描述langchain作用'):
    print(chunk.content, end="", flush=True)
