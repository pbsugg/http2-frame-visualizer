#create http1.1 and http2 instances
#Fake the same user-agent
# Query the same endpoint (simple httpbin.org of various types, more complex site)
# Get all the headers, measure them in raw bits


import httplib
import hyper
from hyper import HTTPConnection

conn = httplib.HTTPConnection("httpbin.org")
conn.request("GET", "/html")
response = conn.getresponse()
response_header = response.msg.__str__()


conn2 = HTTPConnection('http2bin.org')
conn2.request('GET', '/html')
