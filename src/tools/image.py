import time
from http import HTTPStatus

from dashscope import ImageSynthesis
from langchain_core.tools import tool


@tool
def qwen_image_generation(prompt: str) -> str:
    """使用通义万相（Qwen 图像生成模型）根据文本提示生成图像。
    
    Args:
        prompt (str): 图像的详细文本描述（支持中英文，越详细效果越好）。
    
    Returns:
        str: 生成图像的 URL（成功时），或错误信息（失败时）。
    """
    # 提交生成任务
    rsp = ImageSynthesis.call(
        model="wanx-v1",          # 当前常用文生图模型
        prompt=prompt,
        n=1,                      # 生成图片数量（默认1张）
        size="1024*1024"          # 图片分辨率（可选，支持常见尺寸）
    )
    
    if rsp.status_code != HTTPStatus.OK:
        return f"图像生成请求失败: {rsp.message}"
    
    # 获取任务 ID
    task_id = rsp.output.task_id
    
    # 轮询任务状态（通常几秒到几十秒完成）
    while True:
        rsp_status = ImageSynthesis.get_task_status(task_id)
        if rsp_status.status_code != HTTPStatus.OK:
            return "查询任务状态失败"
        
        task_status = rsp_status.output.task_status
        if task_status == "SUCCEEDED":
            # 返回第一张图片的 URL
            return rsp_status.output.results[0].url
        elif task_status in ["FAILED", "CANCELED"]:
            return f"图像生成失败: {rsp_status.output.task_metrics}"
        
        time.sleep(3)  # 每3秒查询一次，避免频繁请求