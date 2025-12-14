from src.state import VideoState

def video_editor_node(state: VideoState):
    """
    合成最终视频
    """
    scenes = state.get("scenes", [])
    print(f"--- [Video Editor] Compiling video from assets ---")
    
    # TODO: Use MoviePy or FFmpeg to stitch images and audio
    
    final_path = "output/final_video.mp4"
    return {"final_video_path": final_path}