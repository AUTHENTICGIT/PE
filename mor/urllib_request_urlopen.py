import urllib.request
import urllib.parse
import socket
import urllib.error

'''data参数'''
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())

'''timeout参数'''
response = urllib.request.urlopen('http://httpbin.org/get', timeout = 1)
print(response.read())

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout = 0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')