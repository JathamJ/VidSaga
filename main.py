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

    db_file = PROJECT_ROOT / "runtime" / f"{title}.pkl"
    file_path = Path(db_file)
    if file_path.exists():
        drama: Drama
        with open(db_file, "rb") as f:
            drama = pickle.load(f)

        # 备份旧状态
        backup_file = PROJECT_ROOT / "runtime" / f"{title}_backup.pkl"
        with open(backup_file, 'wb') as f:
            pickle.dump(drama, f)

        # 继续调试操作
        drama.add_role("西门庆", "")

        for k, role in drama.roles.items():
            print(k, role)
        
        

        # 记录状态
        # with open(db_file, 'wb') as f:
        #     pickle.dump(drama, f)
    else:
        drama_dto = DramaDto(title, desc, style, language, aspect_ratio, scene_time_limit)
        drama = Drama(drama_dto)
        drama.generate_roles()
        with open(db_file, 'wb') as f:
            pickle.dump(drama, f)
    
    
if __name__ == "__main__":
    main()