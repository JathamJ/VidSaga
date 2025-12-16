from src.constants.role import ROLE_JSON
from src.utils.llm_client import get_llm
from src.dto.drama_dto import DramaDto
from src.chains.role import generate_simple_role_chain
import json

# 角色
class Role:
    name: str       # 称呼
    desc: str       # 介绍
    voice_prompt: str   # 音色提示词
    appearance_prompt: str  # 外观提示词

    def __init__(self, name: str, desc: str, voice_prompt: str, appearance_prompt: str):
        self.name = name
        self.desc = desc
        self.voice_prompt = voice_prompt
        self.appearance_prompt = appearance_prompt

    def __str__(self):
        return f"姓名：{self.name}，介绍：{self.desc}，音色提示词：{self.voice_prompt}，外观提示词：{self.appearance_prompt}"

    def generate(self, drama_dto: DramaDto):
        chain = generate_simple_role_chain()
        roles_result = chain.invoke({
            "title": drama_dto.title,
            "desc": drama_dto.desc,
            "style": drama_dto.style,
            "language": drama_dto.language,
            "aspect_ratio": drama_dto.aspect_ratio,
            "role_name": self.name,
            "role_desc": self.desc,
        })

        roles_json = roles_result.content

        print(roles_json)
        role = json.loads(roles_json)
        self = Role(**role)
        return