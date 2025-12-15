class DramaDto:
    title: str  # 标题
    desc: str   # 剧本描述
    style: str  # 画面风格
    language: str  # 语言
    scene_time_limit: int  # 分镜时间限制 单位：秒
    aspect_ratio: str   # 画面比例 例如：16:9

    def __init__(self, title: str, desc: str, style: str, language: str, aspect_ratio: str, scene_time_limit: int):
        self.title = title
        self.desc = desc
        self.style = style
        self.language = language
        self.scene_time_limit = scene_time_limit
        self.aspect_ratio = aspect_ratio