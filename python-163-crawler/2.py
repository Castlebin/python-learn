# encoding: utf-8
# 使用requests和BeautifulSoup实现的简单爬虫结构，爬取新浪国内新闻

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import json

commentURL = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn\
&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8\
&page=1&page_size=20'

def getCommentCounts(newsUrl):
    m = re.search('doc-i(.*).shtml', newsUrl)
    newsId = m.group(1)
    comments = requests.get(commentURL.format(newsId))
    jd = json.loads(comments.text.strip('var data='))

    return jd['result']['count']['total']


def getNewsDetail(newsUrl):
    result = {}
    res = requests.get(newsUrl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    result['title'] = soup.select('#artibodyTitle')[0].text
    result['newsSource'] = soup.select('.time-source span a')[0].contents[0]
    timeSource = soup.select('.time-source')[0].contents[0].strip()
    result['time'] = datetime.strptime(timeSource, '%Y年%m月%d日%H:%M');
    result['article'] = ' '.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])
    result['editor'] = soup.select('.article-editor')[0].text.lstrip('责任编辑：')
    result['comments'] = getCommentCounts(newsUrl)

    return result

newsUrl = 'http://news.sina.com.cn/c/2016-10-27/doc-ifxxfyez2094779.shtml'
print(getNewsDetail(newsUrl))

