from functools import lru_cache
from drama import Drama
from role import Role

class Prompt:

    @staticmethod
    @lru_cache(maxsize=1)
    def get_role_prompt(drama: Drama, role: Role) -> str:
        return f"你是一个提示词工程师，请根据剧情标题：{drama.title}，剧情描述：{drama.desc}，画面风格：{drama.style}，语言：{drama.language}，画面比例：{drama.aspect_ratio}，"
