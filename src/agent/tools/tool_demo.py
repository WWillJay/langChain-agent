from langchain_core.tools import tool
from pydantic import BaseModel, Field

# 方式一
# 默认是方法名
@tool(parse_docstring=True)
def tool_demo(query: str) -> str:
    # 工具的描述：为了大模型根据语义查询适合的根据
    # 谷歌三引号要配合tool注解中的parse_docstring=True使用
    # 或者直接用tool注解中description='描述'
    # Args和Returns前面要空一行
    """互联网搜索工具，可以搜索所有公开的信息。

    Args:
        query: 需要进行互联网查询的信息

    Returns:
        返回搜索的结果，该信息是一个文本字符串
    """
    return '网络异常~~~'


if __name__ == '__main__':
    print(tool_demo.name)
    print(tool_demo.description)
    print(tool_demo.args)
    print(tool_demo.args_schema.model_json_schema())
    result = tool_demo.invoke({'query': '如何学好langchain'})
    print(result)


# 方式二
class SearchArgs(BaseModel):
    query: str = Field(..., description='需要进行互联网查询的信息')


# my_web_search是工具名称，默认是方法名
@tool('my_web_search', args_schema=SearchArgs, description='互联网搜索工具，可以搜索所有公开的信息')
def web_search2(query: str) -> str:
    pass