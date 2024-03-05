# -*- coding: utf-8 -*-
# @Time    : 2024/3/5 15:48
# @Author  : Stepstar
# @FileName: get_report_content.py
# @Software: PyCharm
from get_report_structure import structure
import json
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

report_name = '深度学习在电网领域应用'
#report_structure = structure(report_name)
def write_content(title,intro):
    '''
    :param title: 小标题名称
    :return: gpt返回内容
    '''
    # TODO:加入本地知识库和google search结果
    # TODO:内容加入图片
    # This is an LLMChain to write a content given a title of a play.
    llm = OpenAI()
    template ="""在撰写名为{report_name}的报告，撰写该报告的{title}部分内容,这部分关于{intro}"""
    prompt_template = PromptTemplate(input_variables=["report_name","title","intro"], template=template)
    synopsis_chain = LLMChain(llm=llm, prompt=prompt_template)
    return synopsis_chain.run({"report_name":report_name ,"title":title,"intro":intro})
m = write_content("电网系统概述", "解释电网的基础结构，包括发电、传输、配电和用户消费等环节。讨论电网面临的关键挑战，如需求预测、资产管理、故障检测和电能质量分析等。")
# TODO:优化返回的值
'''
返回值缺失
'''
