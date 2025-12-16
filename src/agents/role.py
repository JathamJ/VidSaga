from src.constants.role import ROLE_JSON
from src.utils.llm_client import get_llm
from src.dto.drama_dto import DramaDto
from src.chains.role import generate_simple_role_chain
import json
from src.utils.resolution import get_aspect_ratio_resolution
from src.prompts.role import get_role_model_image_prompt_template

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
        role = json.loads(roles_json)
        self.name = role['name']
        self.desc = role['desc']
        self.voice_prompt = role['voice_prompt']
        self.appearance_prompt = role['appearance_prompt']
        return

    def get_appearance_img_prompt(self, drama_dto: DramaDto) -> str:
        """根据风格和宽高比获取角色的外观提示词。"""

        image_size = get_aspect_ratio_resolution(drama_dto.aspect_ratio)

        prompt = get_role_model_image_prompt_template().format(
            style=drama_dto.style,
            aspect_ratio=drama_dto.aspect_ratio,
            role_name=self.name,
            appearance_prompt=self.appearance_prompt,
            image_size=image_size,
        )
        return prompt