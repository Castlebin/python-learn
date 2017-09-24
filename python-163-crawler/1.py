#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 使用requests和BeautifulSoup实现的简单爬虫结构，爬取新浪国内新闻"""

import requests
from bs4 import BeautifulSoup

res = requests.get('http://news.sina.com.cn/china/')
# print(res.encoding)

res.encoding = 'utf-8'
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.text)

for news in soup.select('.news-item'):  # select拿出来的是一个数组
    if len(news.select('h2')) > 0:  # select拿出来的是一个数组
        h2 = news.select('h2')[0].text
        a = news.select('a')[0]['href']
        time = news.select('.time')[0].text
        print(h2, a, time)
