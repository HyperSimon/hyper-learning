# FileCookieJar

import cookielib
import urllib2

filename = 'cookie.txt'

cookie = cookielib.MozillaCookieJar(filename)

handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)

response = opener.open('http://www.baidu.com')

cookie.save(ignore_discard=True, ignore_expires=True)
# ignore_discard: save even cookies set to be discarded.
# ignore_expires: save even cookies that have expiredThe file is overwritten if it already exists
