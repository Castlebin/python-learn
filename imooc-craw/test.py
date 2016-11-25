#! /usr/bin/env python
# encoding: utf-8

import urllib2
import cookielib

url = 'http://www.baidu.com/'
# method one
response = urllib2.urlopen(url)
print response.getcode()
print len(response.read())

# method two
request = urllib2.Request(url)
request.add_header("User-Agent", "Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

# method three
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
print len(response3.read())
