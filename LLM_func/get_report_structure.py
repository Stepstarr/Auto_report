# -*- coding: utf-8 -*-
# @Time    : 2024/3/5 14:22
# @Author  : Stepstar
# @FileName: get_report_structure.py
# @Software: PyCharm
# v1.0简单调用获得报告结构
from langchain.memory import ConversationBufferMemory
from langchain import OpenAI, LLMChain, PromptTemplate
import json
def check(text): #将GPT返回内容转为dict格式
    import re
    # 正则表达式
    pattern = r'\{.*\}'

    # 使用正则表达式搜索
    match = re.search(pattern, text, re.DOTALL)

    # 提取和打印匹配的内容
    if match:
        content = match.group()  # group(1) 返回括号内匹配的文本
        return json.loads(content)
    else:
        print("No match found.")

def structure(report_name):
    template = """写名为{report_name}的报告，这个报告可以分哪几大块，并文字概述各个大块应写什么，注意：返回字典形式，键是每个大块的标题，值是该大块需写一些什么，无需返回其他"""
    prompt = PromptTemplate(
        input_variables=["report_name"],
        template=template
    )
    # TODO:该处用的openai==0.28,否则加model_name错误，新版openai待适配
    '''
    Q：后续提取严格依赖gpt返回质量，如何解决当GPT返回格式不当的情况
    '''
    #memory = ConversationBufferMemory(memory_key="chat_history")
    llm_chain = LLMChain(
        llm=OpenAI(model_name="gpt-4-turbo-preview"),
        prompt=prompt,
        verbose=True,
        #memory=memory,
    )
    stucture_result = llm_chain.run(report_name)
    print(stucture_result)
    stucture_result_final = check(str(stucture_result))
    return stucture_result_final
result = structure("深度学习在电网中的应用")
# TODO:序列链在下面加一个prompt保证格式统一
# This is an LLMChain to write a synopsis given a title of a play and the era it is set in.
# llm = OpenAI()
# template="""写名为{report_name}的报告，这个报告可以分哪几大块，并文字概述各个大块应写什么，注意：返回以json形式，键是每个大块的标题，值是该大块需写一些什么，无需返回其他"""
# prompt1 = PromptTemplate(
#         input_variables=["report_name"],
#         template=template
#     )
#
# structure_chain = LLMChain(llm=llm, prompt=prompt1, output_key="structure")
# # This is an LLMChain to write a review of a play given a synopsis.
# llm = OpenAI()
# template2 = """把下面这段内容提取出其中的字典格式的东西并返回为为字典格式
# 内容如下:{structure}"""
# prompt2 = PromptTemplate(input_variables=["structure"], template=template2)
# review_chain = LLMChain(llm=llm, prompt=prompt2, output_key="dict_structure")
# # This is the overall chain where we run these two chains in sequence.
# from langchain.chains import SimpleSequentialChain
#
# overall_chain = SimpleSequentialChain(chains=[structure_chain, review_chain], verbose=True)
# review = overall_chain.run("深度学习在电网中的应用")

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