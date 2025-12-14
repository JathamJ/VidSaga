from src.constants.role import ROLE_JSON
from src.utils.llm_client import get_llm
from drama import Drama

# 角色
class Role:
    name: str
    desc: str
    voice_prompt: str
    appearance_prompt: str

    def __init__(self, name: str, desc: str, voice_prompt: str, appearance_prompt: str):
        self.name = name
        self.desc = desc
        self.voice_prompt = voice_prompt
        self.appearance_prompt = appearance_prompt

    def generate(self, drama: Drama) -> bool:
        prompt = f"你是一个AI编剧-提示词工程师，请根据剧情标题：{drama.title}，剧情描述：{drama.desc}，画面风格：{drama.style}，语言：{drama.language}，画面比例：{drama.aspect_ratio}，生成角色: 姓名：{self.name}，介绍：{self.desc}。请以以下json结构返回：{ROLE_JSON}，请直接输出json字符串，不要包含任何其他文本。"

        roles_result = get_llm().invoke(prompt)
        roles_json = roles_result.content
        role = json.loads(roles_json)

        self.name = role.name
        self.desc = role.desc
        self.voice_prompt = role.voice_prompt
        self.appearance_prompt = role.appearance_prompt
        return True