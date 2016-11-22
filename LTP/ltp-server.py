# -*- coding: utf-8 -*-
#!/usr/bin/env python
import urllib, urllib2

uri_base = "http://127.0.0.1:12345/ltp"

data = {
    's': '我爱北京天安门',
    'x': 'n',
    't': 'all'}

request = urllib2.Request(uri_base)
params = urllib.urlencode(data)
response = urllib2.urlopen(request, params)
content = response.read().strip()
print content