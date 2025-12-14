from src.state import VideoState, Scene

def storyboard_artist_node(state: VideoState):
    """
    将剧本拆解为分镜
    """
    script = state.get("script", "")
    print(f"--- [Storyboard Artist] Creating scenes from script ---")
    
    # TODO: Parse script and generate structured scenes using LLM
    
    # Mock output
    scenes = [
        Scene(scene_id=1, narration="这是一个晴朗的早晨", visual_desc="阳光明媚的公园，有人在晨跑", image_path=None, audio_path=None),
        Scene(scene_id=2, narration="突然，天空暗了下来", visual_desc="乌云密布的天空，雷电交加", image_path=None, audio_path=None)
    ]
    
    return {"scenes": scenes}