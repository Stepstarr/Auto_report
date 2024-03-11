# -*- coding: utf-8 -*-
# @Time    : 2024/3/5 10:18
# @Author  : Stepstar
# @FileName: search_func.py
# @Software: PyCharm
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper
import os
# Set the http_proxy and https_proxy environment variables
proxy_url = 'http://127.0.0.1'
proxy_port = '7890'

os.environ['http_proxy'] = f'{proxy_url}:{proxy_port}'
os.environ['https_proxy'] = f'{proxy_url}:{proxy_port}'
os.environ["GOOGLE_CSE_ID"] = "e485b8380c5fe423f"
os.environ["GOOGLE_API_KEY"] = "AIzaSyA17AyyJUrYYJOurE1h8DNg9StxP-cj0Kk"
# TODO:向谷歌问什么问题
search = GoogleSearchAPIWrapper(k=3)
def topk_results(query,k):
    return search.results(query, k)

def google_search(query):
    tool = Tool(
        name="Google Search Snippets",
        description="Search Google for recent results.",
        func=topk_results
    )

    m = tool.run(query)
    return m
