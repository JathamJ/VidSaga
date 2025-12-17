from typing import List
from src.agents.shot import Shot



class Scene:
    key_action: str # 衔接关键操作
    name: str # 场景名称
    time: str # 场景时间
    location: str # 场景地点
    events: str # 场景事件
    results: str # 场景结果
    scene_prompt: str # 场景描述
    roles: List[str] # 场景中的角色
    before_summary: str # 剧情-前情提要
    bg_voice: str # 背景语音 场景中环境的声音，如风声、雨声、雨声等
    shots: List[Shot] # 场景中的镜头
    next_scene: None # 下一场景
    
    def __init__(self, key_action: str, name: str, time: str, location: str, events: str, roles: List[str], before_summary: str):
        self.key_action = key_action
        self.name = name
        self.time = time
        self.location = location
        self.events = events
        self.roles = roles
        self.before_summary = before_summary

    def generate_shots(self):
        return