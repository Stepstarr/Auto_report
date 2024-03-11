# -*- coding: utf-8 -*-
# @Time    : 2024/3/6 14:15
# @Author  : Stepstar
# @FileName: Auto_report_streamlit.py
# @Software: PyCharm
proxy_url = 'http://127.0.0.1'
proxy_port = '7890'
import os
os.environ['http_proxy'] = f'{proxy_url}:{proxy_port}'
os.environ['https_proxy'] = f'{proxy_url}:{proxy_port}'
from LLM_func.get_report_content import all_content
from report_format.output import output
import streamlit as st
from docx import Document
from io import BytesIO
with st.sidebar:
    # TODO:优化页面
    st.title('欢迎来到我的应用')
    st.subheader('选择模型')
    streaming = st.checkbox('ChatGPT4', True)
    in_expander = st.checkbox('Llama2',False)
    show_history = st.checkbox('ChatGLM', False)


    st.markdown('---')
    st.button('本地知识库')
    st.markdown('在该模块可以导入本地知识，优化报告生成')


import time  # 用于模拟报告生成过程

# 定义生成docx文件的函数
def create_docx(report_name):
    # 模拟长时间运行的过程
    m = all_content(report_name)
    report =output(m, 'test', report_name)
    # time.sleep(5)  # 假设报告生成需要5秒钟
    # doc = Document()
    # doc.add_paragraph(content)
    return report


# Streamlit应用界面
st.title('这是主界面')
st.write('Hello, *World!* :sunglasses: 本项目旨在基于LLM进行行业报告的智能生成，LLM is all you need!')
st.info('请输入所需撰写的报告名称并点击按钮生成docx文件')

# 创建输入框
user_input = st.text_input('请输入报告名称')

# 创建消息占位符
status_placeholder = st.empty()

# 创建按钮，并在点击后执行函数
if st.button('生成报告文件'):
    with st.spinner('正在生成中请等待...'):
        # 使用输入的内容生成docx文件
        doc = create_docx(user_input)

        # 将生成的docx文件转换为二进制流，以便下载
        byte_io = BytesIO()
        doc.save(byte_io)
        byte_io.seek(0)

        # 更新消息占位符的状态
        status_placeholder.success('生成成功！')

    # 提供下载链接
    st.download_button(label='下载Docx文件',
                       data=byte_io,
                       file_name='download.docx',
                       mime='application/vnd.openxmlformats-officedocument.wordprocessingml.document')