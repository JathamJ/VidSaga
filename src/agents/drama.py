from typing import Dict
from src.agents.role import Role
import json
from src.chains.role import generate_role_chain
from src.dto.drama_dto import DramaDto
from src.agents.scene import Scene
from src.chains.scene import generate_scene_chain


# 剧本
class Drama:
    drama_dto: DramaDto
    roles: Dict[str, Role]  # 角色
    first_scene: Scene # 第一场景

    def __init__(self, drama_dto: DramaDto):
        self.drama_dto = drama_dto
        self.roles = {} # 初始化角色字典

    def get_all_role_desc(self) -> str:
        result = ''
        for _, role in self.roles.items():
            result += role.name + ':' + role.desc + '\n'
        return result

    def generate_roles(self) -> Dict[str, Role]:
        chain = generate_role_chain()
        roles_result = chain.invoke({
            "title": self.drama_dto.title,
            "desc": self.drama_dto.desc,
            "style": self.drama_dto.style,
            "language": self.drama_dto.language,
            "aspect_ratio": self.drama_dto.aspect_ratio
        })
        roles_json = roles_result.content
        role_arr = json.loads(roles_json)

        for role in role_arr:
            self.roles[role["name"]] = Role(role["name"], role["desc"], role["voice_prompt"], role["appearance_prompt"])
        return self.roles

    def add_role(self, name: str, desc: str):
        role = Role(name, desc, "", "")
        role.generate(self.drama_dto)
        self.roles[role.name] = role
        return role

    def generate_first_scene(self):
        chain = generate_scene_chain()
        scene_result = chain.invoke({
            "title": self.drama_dto.title,
            "desc": self.drama_dto.desc,
            "style": self.drama_dto.style,
            "language": self.drama_dto.language,
            "aspect_ratio": self.drama_dto.aspect_ratio,
            "roles": self.get_all_role_desc(),
            "prev_scene": "无（第一场景）",
        })
        
        scene_json = scene_result.content
        scene = json.loads(scene_json)

        self.first_scene = Scene(
            "", 
            scene["name"], 
            scene["time"], 
            scene["location"], 
            scene["events"], 
            scene["roles"], 
            "",
        )
        return self.first_scene



