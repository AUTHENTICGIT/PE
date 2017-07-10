import urllib.request

request = urllib.request.urlopen('http://www.weibo.com')
print(type(request))    # 获取对象类型是HTTPResponse

# status属性
print(request.status)   # 得到返回结果的状态码，200表示成功，404表示未找到

# msg属性
print(request.msg)


# read()方法
print(request.read())   # 得到返回的网页内容

# getheaders()方法
print(request.getheaders()) # 得到响应头信息

#getheader(name)方法
print(request.getheader('Server'))  # 通过传递一个Server参数，获取了headers中的Server值
print(request.getheader('Date'))
print(request.getheader('Cache-Control'))

