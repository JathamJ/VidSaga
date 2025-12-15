from typing import Dict
from src.agents.role import Role
import json
from src.chains.role import generate_role_chain
from src.dto.drama_dto import DramaDto


# 剧本
class Drama:
    drama_dto: DramaDto
    roles: Dict[str, Role]  # 角色

    def __init__(self, drama_dto: DramaDto):
        self.drama_dto = drama_dto

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

        print(roles_json)

        role_arr = json.loads(roles_json)

        for role in role_arr:
            self.roles[role["name"]] = Role(role["name"], role["desc"], role["voice_prompt"], role["appearance_prompt"])
        return self.roles

    def add_role(self, name: str, desc: str):
        role = Role(name, desc, "", "")
        return role.generate(role, self)



