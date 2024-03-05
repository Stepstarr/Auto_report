# -*- coding: utf-8 -*-
# @Time    : 2024/3/5 14:22
# @Author  : Stepstar
# @FileName: get_report_structure.py
# @Software: PyCharm
from langchain.memory import ConversationBufferMemory
from langchain import OpenAI, LLMChain, PromptTemplate
def structure(report_name):
    template = """写名为{report_name}的报告，除了开头的绪论，这个报告可以分哪几大块，并文字概述各个大块应写什么，注意：返回以字典形式，键是每个大块的标题，值是该大块需写一些什么"""
    prompt = PromptTemplate(
        input_variables=["report_name"],
        template=template
    )
    # TODO:该处用的openai==0.28,否则加model_name错误，新版openai待适配
    '''
    Q：后续提取严格依赖gpt返回质量，如何解决当GPT返回格式不当的情况
    '''
    memory = ConversationBufferMemory(memory_key="chat_history")
    llm_chain = LLMChain(
        llm=OpenAI(model_name="gpt-4-turbo-preview"),
        prompt=prompt,
        verbose=True,
        memory=memory,
    )
    stucture_result = llm_chain.run(report_name)
    return stucture_result

# template = """写名为{report_name}的报告，除了开头的绪论，这个报告可以分哪几大块，并文字概述各个大块应写什么，注意：返回以字典形式，键是每个大块的标题，值是该大块需写一些什么"""
# prompt = PromptTemplate(
#     input_variables=["report_name"],
#     template=template
# )
# memory = ConversationBufferMemory(memory_key="chat_history")
# llm_chain = LLMChain(
#     llm=OpenAI( model_name="gpt-4-turbo-preview"),
#     prompt=prompt,
#     verbose=True,
#     memory=memory,
# )
# m = llm_chain.run('电网中深度学习的应用')