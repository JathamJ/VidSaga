import os
from dotenv import load_dotenv
from src.agents.drama import Drama
import sys

# Load environment variables
load_dotenv()

def main():
    print("Initializing VidSaga AI Short Video Generator...")
    
    title = input("请输入名称: ")
    if not title:
        title = os.getenv("TEMP_TITLE")
        if not title:
            sys.exit("未输入名称")

    desc = input("请输入描述: (包括：剧情梗概、场景描述，结局等)")
    if not desc:
        desc = os.getenv("TEMP_DESC")
        if not desc:
            sys.exit("未输入描述")

    style = input("请输入画面整体风格: ")
    if not style:
        style = "写实"

    language = os.getenv("VIDEO_MAIN_LANGUAGE")
    if not language:
        language = "中文"
    
    scene_time_limit = int(os.getenv("VIDEO_SLICE_TIME_LIMIT"))
    if not scene_time_limit:
        scene_time_limit = 10
    
    aspect_ratio = os.getenv("VIDEO_ASPECT_RATIO")
    if not aspect_ratio:
        aspect_ratio = "9:16"

    drama = Drama(title, desc, style, language, aspect_ratio, scene_time_limit)
    
    roles_result = drama.generate_roles()
    print(roles_result.content)
    
if __name__ == "__main__":
    main()