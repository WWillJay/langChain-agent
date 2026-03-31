from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

from agent.llms import llm_openai

# 提示词模板
prompt = ChatPromptTemplate.from_template(
    """回答用户查询时，严格按照以下要求输出：
    1. 仅返回JSON格式数据，不要添加任何额外文字
    2. JSON必须包含且仅包含三个字段：title（电影名）、year（上映年份）、director（导演）
    3. 字段值必须准确，格式正确
    用户问题：{question}"""
)
chain = prompt | llm_openai | JsonOutputParser()
response = chain.invoke({"question": "提供电影《泰坦尼克号》详情"})
print(response)