# coding: utf-8

import urllib2
import cookielib

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open('http://weibo.com/u/3932449890/home?wvr=5')  # 获取 cookie

req = urllib2.Request('http://weibo.com/u/3932449890/home?wvr=5')

req.add_header('Host', 'weibo.com')
req.add_header('Proxy-Connection', 'keep-alive')
req.add_header('Referer', 'https://www.baidu.com/link?url=ClVDpEA3n8kTz2GMaiHrO8OKzzCTQFODyQS5Ns13fs_&wd=&eqid=c777458a00045bd00000000658b76bff')
req.add_header('Upgrade-Insecure-Requests', '1')
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')

cookies = []
for item in cookie:
    cookies.append(item.name + '=' + item.value)
    # cookies.append(item.name + '=' + item.value)
req.add_header('Cookie', ';'.join(cookies))

req.add_data('s')

print req.headers
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)

print response.read()
