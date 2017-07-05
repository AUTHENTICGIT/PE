import re

reTestStr = u'标签：<a href="/tag/情侣电话粥/">情侣电话粥</a>'
foundTagA = re.search(u'.+?<a href="/tag/(?P<tagName>.+?)/">(?P=tagName)</a>', reTestStr)
print('founTagA =', foundTagA)
print('founTagA =', foundTagA.group(1))