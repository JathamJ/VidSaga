from langchain_core.prompts import ChatPromptTemplate


def create_chain(prompt_template: str, llm: ChatOpenAI):
    prompt = ChatPromptTemplate.from_template(prompt_template)
    chain = prompt | llm

    chain.invoke({"input": "你好"})
    return chain