from langchain_core.prompts import ChatPromptTemplate
from src.constants.role import ROLE_JSON

def get_role_prompt_template() -> ChatPromptTemplate:
    # 转义 ROLE_JSON 中的花括号，避免被识别为模板变量
    escaped_role_json = ROLE_JSON.replace('{', '{{').replace('}', '}}')
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个AI编剧助手-角色塑造大师，你会根据剧情描述和画面风格，分析推测可能出现的角色，生成详细的角色描述。"),
        ("user", "剧情标题：{title}"),
        ("user", "剧情描述：{desc}"),
        ("user", "画面风格：{style}"),
        ("user", "语言：{language}"),
        ("user", "画面比例：{aspect_ratio}"),
        ("system", f"请根据以上信息，生成角色描述，以下json结构返回：[{escaped_role_json}]"),
        ("system", "请直接输出json字符串，不要包含任何其他文本。"),
    ])
    return prompt

def get_simple_role_prompt_template() -> ChatPromptTemplate:
    # 转义 ROLE_JSON 中的花括号，避免被识别为模板变量
    escaped_role_json = ROLE_JSON.replace('{', '{{').replace('}', '}}')
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个AI编剧助手-角色塑造大师，你会根据剧情描述和画面风格，出现的角色，生成详细的角色描述。"),
        ("user", "剧情标题：{title}"),
        ("user", "剧情描述：{desc}"),
        ("user", "画面风格：{style}"),
        ("user", "语言：{language}"),
        ("user", "画面比例：{aspect_ratio}"),
        ("user", "角色名：{role_name}"),
        ("user", "角色描述：{role_desc}"),
        ("system", f"请根据以上信息，生成角色描述，以下json结构返回：{escaped_role_json}"),
        ("system", "请直接输出json字符串，不要包含任何其他文本。"),
    ])
    return prompt