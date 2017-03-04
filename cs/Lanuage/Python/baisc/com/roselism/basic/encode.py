# coding=utf-8

import urllib

values = {}
values['username'] = '1000000@qq.com'
values['password'] = '我叫王镇'

data = urllib.urlencode(values)  # url 加密字符串
print data
