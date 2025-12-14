import os
from functools import lru_cache
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# 确保环境变量已加载
load_dotenv()

class LLMManager:
    """
    大模型资源管理器，负责初始化和管理 LLM 客户端实例。
    """
    
    @staticmethod
    @lru_cache(maxsize=1)
    def get_openai_client(temperature: float = 1.0) -> ChatOpenAI:
        """
        获取 OpenAI Chat 客户端单例 (带缓存)
        
        Args:
            model_name: 模型名称，默认为 "gpt-3.5-turbo"
            temperature: 温度参数，控制生成随机性
            
        Returns:
            ChatOpenAI 实例
        """
        api_key = os.getenv("OPENAI_API_KEY")
        model_name = os.getenv("OPENAI_LLM_MODEL")
        base_url = os.getenv("OPENAI_LLM_URL")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables.")
            
        print(f"--- [LLM Manager] Initializing OpenAI Client ({model_name}) ---")
        return ChatOpenAI(
            model=model_name,
            temperature=temperature,
            api_key=api_key,
            base_url=base_url,
            max_tokens=40960
        )

# 便捷访问函数
def get_llm(temperature: float = 1.0) -> ChatOpenAI:
    return LLMManager.get_openai_client(temperature)
