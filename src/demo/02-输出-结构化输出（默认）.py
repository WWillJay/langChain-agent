from pydantic import BaseModel, Field
from agent.llms import llm_openai

# 不是所有模型都支持
class Movie(BaseModel):
    """电影详情结构化数据"""
    title: str = Field(..., description="电影标题（中文）")
    year: str = Field(..., description="电影发行年份（纯数字）")
    rating: str = Field(..., description="电影评分（满分10分，如 9.5）")
    director: str = Field(..., description="电影导演（可选，补充字段）")

with_structured_output = llm_openai.with_structured_output(Movie)
response = with_structured_output.invoke("提供电影《泰坦尼克号》详情")
print(response)