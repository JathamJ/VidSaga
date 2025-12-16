
def get_aspect_ratio_resolution(aspect_ratio: str) -> str:
    """根据宽高比获取图片分辨率。"""
    if aspect_ratio == "9:16":
        return "1024*1366"
    elif aspect_ratio == "16:9":
        return "1366*1024"
    else:
        return "1024*1024"