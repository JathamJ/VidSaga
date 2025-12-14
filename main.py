import os
from dotenv import load_dotenv
from src.graph import create_graph

# Load environment variables
load_dotenv()

def main():
    print("Initializing VidSaga AI Short Video Generator...")
    
    app = create_graph()
    
    topic = input("请输入短剧主题: ")
    if not topic:
        topic = "A cyberpunk detective story in Neo-Tokyo"
    
    initial_state = {
        "topic": topic,
        "script": None,
        "scenes": [],
        "final_video_path": None,
        "current_step": "start",
        "errors": []
    }
    
    print(f"Starting workflow for topic: {topic}")
    
    # Run the graph
    for output in app.stream(initial_state):
        for key, value in output.items():
            print(f"Finished step: {key}")
            # print(f"Output: {value}") # Uncomment to see full state updates

    print("Workflow completed.")

if __name__ == "__main__":
    main()