#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import json

commentURL = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn\
&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8\
&page=1&page_size=20'


def get_comment_counts(newsUrl):
    m = re.search('doc-i(.*).shtml', newsUrl)
    news_id = m.group(1)
    comments = requests.get(commentURL.format(news_id))
    jd = json.loads(comments.text.strip('var data='))

    return jd['result']['count']['total']


def get_news_detail(newsUrl):
    result = {}
    res = requests.get(newsUrl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    result['title'] = soup.select('#artibodyTitle')[0].text
    result['newsSource'] = soup.select('.time-source span a')[0].contents[0]
    time_source = soup.select('.time-source')[0].contents[0].strip()
    result['time'] = datetime.strptime(time_source, '%Y年%m月%d日%H:%M')
    result['article'] = ' '.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])
    result['editor'] = soup.select('.article-editor')[0].text.lstrip('责任编辑：')
    result['comments'] = get_comment_counts(newsUrl)

    return result


newsUrl = 'http://news.sina.com.cn/c/2016-10-27/doc-ifxxfyez2094779.shtml'
print(get_news_detail(newsUrl))

