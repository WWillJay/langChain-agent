from langchain_core.tools import tool

@tool(parse_docstring=True)
def web_search(query: str) -> str:
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