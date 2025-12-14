from typing import List, TypedDict, Optional, Annotated
import operator

class Scene(TypedDict):
    scene_id: int
    narration: str  # 旁白/台词
    visual_desc: str # 画面描述
    image_path: Optional[str]
    audio_path: Optional[str]

class VideoState(TypedDict):
    """
    VidSaga 项目的状态定义
    """
    topic: str
    script: Optional[str]
    scenes: List[Scene]
    final_video_path: Optional[str]
    current_step: str
    errors: List[str]
