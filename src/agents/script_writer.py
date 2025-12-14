from langchain_core.messages import SystemMessage, HumanMessage
from src.state import VideoState
from src.utils.llm_client import get_llm

def script_writer_node(state: VideoState):
    """
    根据主题生成短剧剧本
    """
    topic = state["topic"]
    print(f"--- [Script Writer] Generating script for topic: {topic} ---")
    
    try:
        llm = get_llm()
        
        messages = [
            SystemMessage(content="You are a professional short video script writer. Create a compelling script based on the user's topic."),
            HumanMessage(content=f"Write a short video script about: {topic}")
        ]
        
        response = llm.invoke(messages)
        generated_script = response.content
        
    except Exception as e:
        print(f"Error generating script: {e}")
        # Fallback for testing without API key or network
        generated_script = f"剧本标题: {topic}\n\n(Generated via Fallback)\n场景1: 开场...\n场景2: 发展..."
    
    return {"script": generated_script}
