from typing import List

class Scene:
    scene_prompt: str # 场景描述
    roles: List[str] # 场景中的角色
    before_summary: str # 剧情-前情提要
    bg_voice: str # 背景语音 场景中环境的声音，如风声、雨声、雨声等
