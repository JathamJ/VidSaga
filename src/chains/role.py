from functools import lru_cache
from src.prompts.role import get_role_prompt_template
from src.utils.llm_client import get_llm
from langchain_core.runnables import Runnable

@lru_cache(maxsize=1)
def generate_role_chain() -> Runnable:
    prompt = get_role_prompt_template()
    llm = get_llm()
    return prompt | llm