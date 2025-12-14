from langchain_core.messages import SystemMessage, HumanMessage
from src.state import VideoState

def script_writer_node(state: VideoState):
    """
    根据主题生成短剧剧本
    """
    topic = state["topic"]
    print(f"--- [Script Writer] Generating script for topic: {topic} ---")
    
    # TODO: Integrate with actual LLM
    # prompt = f"Write a short video script about: {topic}"
    
    # Mock output
    generated_script = f"剧本标题: {topic}\n\n场景1: 开场...\n场景2: 发展..."
    
    return {"script": generated_script}
