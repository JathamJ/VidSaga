import os
from pathlib import Path
from dotenv import load_dotenv
from src.agents.drama import Drama
from src.dto.drama_dto import DramaDto
import sys
import pickle
from src.constants.path import PROJECT_ROOT

# Load environment variables
load_dotenv()

def main():
    print("Initializing VidSaga AI Short Video Generator...")
    
    title = os.getenv("STORY_TITLE")
    desc = os.getenv("STORY_DESC")

    if not title or not desc:
        sys.exit("Please input title and desc!")

    style = os.getenv("STORY_STYLE")
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

    db_file = PROJECT_ROOT / "runtime" / f"{title}.pkl"
    file_path = Path(db_file)
    if file_path.exists():
        drama: Drama
        with open(db_file, "rb") as f:
            drama = pickle.load(f)
        drama.drama_dto.desc = desc

        # 备份旧状态
        backup_file = PROJECT_ROOT / "runtime" / f"{title}_backup.pkl"
        with open(backup_file, 'wb') as f:
            pickle.dump(drama, f)

        # 继续调试操作
        drama.generate_first_scene()
        
        # 记录状态
        with open(db_file, 'wb') as f:
            pickle.dump(drama, f)
    else:
        drama_dto = DramaDto(title, desc, style, language, aspect_ratio, scene_time_limit)
        drama = Drama(drama_dto)
        drama.generate_roles()
        with open(db_file, 'wb') as f:
            pickle.dump(drama, f)
    
    
if __name__ == "__main__":
    main()