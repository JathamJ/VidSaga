from src.state import VideoState

def audio_creator_node(state: VideoState):
    """
    为每个分镜生成语音
    """
    scenes = state.get("scenes", [])
    print(f"--- [Audio Creator] Generating audio for {len(scenes)} scenes ---")
    
    new_scenes = []
    for scene in scenes:
        # TODO: Call TTS API (e.g. OpenAI TTS, ElevenLabs)
        
        # Mock path
        scene['audio_path'] = f"output/audio/scene_{scene['scene_id']}.mp3"
        new_scenes.append(scene)
    
    return {"scenes": new_scenes}