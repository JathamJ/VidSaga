from langgraph.graph import StateGraph, END
from src.state import VideoState
from src.agents.script_writer import script_writer_node
from src.agents.storyboard_artist import storyboard_artist_node
from src.agents.visual_creator import visual_creator_node
from src.agents.audio_creator import audio_creator_node
from src.agents.video_editor import video_editor_node

def create_graph():
    workflow = StateGraph(VideoState)

    # Add nodes
    workflow.add_node("script_writer", script_writer_node)
    workflow.add_node("storyboard_artist", storyboard_artist_node)
    workflow.add_node("visual_creator", visual_creator_node)
    workflow.add_node("audio_creator", audio_creator_node)
    workflow.add_node("video_editor", video_editor_node)

    # Define edges
    workflow.set_entry_point("script_writer")
    workflow.add_edge("script_writer", "storyboard_artist")
    workflow.add_edge("storyboard_artist", "visual_creator")
    workflow.add_edge("visual_creator", "audio_creator")
    workflow.add_edge("audio_creator", "video_editor")
    workflow.add_edge("video_editor", END)

    return workflow.compile()
