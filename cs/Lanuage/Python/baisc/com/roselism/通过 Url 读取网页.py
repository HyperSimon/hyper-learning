# coding=utf-8
# import urllib
#
# def getHtml(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     return html
#
# html = getHtml("http://tieba.baidu.com/p/2738151262")
#
# print html

import re
import urllib


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg' % x)
        x += 1
        # return imglist


html = getHtml('http://tieba.baidu.com/p/2460150866')
print getImg(html)
