import urllib2
import cookielib

cookie = cookielib.CookieJar()

handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)

response = opener.open('http://www.baidu.com')


def printKV(k, v):
    print 'key = ' + item.name + ' value = ' + v


for item in cookie:
    printKV(item.name, item.value)


# -------- output --------
# key = BAIDUID value = 4C3D6E7B294F654CE970D25AF87FD1F9:FG=1
# key = BIDUPSID value = 4C3D6E7B294F654CE970D25AF87FD1F9
# key = H_PS_PSSID value = 22161_1463_19035_21081_18559_17001_22037_22174_20929
# key = PSTM value = 1488391918
# key = BDSVRTM value = 0
# key = BD_HOME value = 0
