from langchain_core.prompts import ChatPromptTemplate
from src.constants.scene import SCENE_TREE_JSON

def get_scene_prompt_template() -> ChatPromptTemplate:

    escaped_scene_tree_json = SCENE_TREE_JSON.replace('{', '{{').replace('}', '}}')

    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个AI编剧助手，你会根据规则描述和前情提要，继续编写场景剧本。场景无需包含所有角色，只需要包含场景中需要出现的角色即可。"),
        ("system", "全局主要角色及角色描述：{roles}"),
        ("system", "每个场景都必须包含场景描述、场景时间、场景地点、场景人物（从用户输入角色中选择，或无任务纯旁白场景）、场景事件、场景结果、衔接关键操作（可以是对话、人物决策等）。"),
        ("system", "下一场景要包含多种剧情发展方向，不同的发展分支会造成不同的剧本结果"),
        ("user", "剧本标题：{title}"),
        ("user", "规则描述：{desc}"),
        ("user", "前情提要：{prev_scene}"),
        ("user", "语言：{language}"),
        ("system", f"请以以下json结构返回：{escaped_scene_tree_json}"),
        ("system", "请直接输出合法的json字符串，不要包含任何其他文本。"),
    ])
    return prompt
