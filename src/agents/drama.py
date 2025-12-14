from typing import Dict
from src.agents.role import Role
from src.constants.role import ROLE_JSON
from src.utils.llm_client import get_llm
import json

# 剧本
class Drama:
    title: str
    desc: str
    style: str
    language: str
    scene_time_limit: int
    aspect_ratio: str
    roles: Dict[str, Role]

    def __init__(self, title: str, desc: str, style: str, language: str, aspect_ratio: str, scene_time_limit: int):
        self.title = title
        self.desc = desc
        self.style = style
        self.language = language
        self.scene_time_limit = scene_time_limit
        self.aspect_ratio = aspect_ratio

    def generate_roles(self) -> Dict[str, Role]:

        prompt = f"你是一个AI编剧-提示词工程师，请根据剧情标题：{self.title}，剧情描述：{self.desc}，画面风格：{self.style}，语言：{self.language}，画面比例：{self.aspect_ratio}，生成剧本可能出现的角色。请以以下json结构返回：[{ROLE_JSON}]，请直接输出json字符串，不要包含任何其他文本。"

        roles_result = get_llm().invoke(prompt)
        roles_json = roles_result.content
        role_arr = json.loads(roles_json)

        for role in role_arr:
            self.roles[role["name"]] = Role(role["name"], role["desc"], role["voice_prompt"], role["appearance_prompt"])
        return self.roles

    def add_role(self, name: str, desc: str):
        role = Role(name, desc, "", "")
        return role.generate()



