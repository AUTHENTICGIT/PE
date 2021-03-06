import re
import datetime

text = 'output_1981.10.21.txt'
m = re.search('output_(\d{4}).(\d{2}).(\d{2})',text)
yy = m.group(1)
mm = m.group(2)
dd = m.group(3)

n = re.search('output_(?P<year>\d{4}).(\d{2}).(?P<day>\d\d)', text)
print(n.group())
print(n.group('year'))
print(n.group(2))
print(n.group('day'))

# mp = re.search('output_(?P<line>(\d{4}).(\d{2}).(\d{2}))',text)
# print('line =', mp.group('line'))
# x = re.match('(\d+)(\d+)(\d+)', '1982.10.21')
# print(x.group(1))
# print(x.group(2))
# print(x.group(3))


day = datetime.datetime(int(yy), int(mm), int(dd)).strftime('%w')

def get_week_day(date):
    week_day = {
        1:'星期一',
        2:'星期二',
        3:'星期三',
        4:'星期四',
        5:'星期五',
        6:'星期六',
        0:'星期日'
    }
    return week_day[int(date)]

print(yy + '年' + mm + '月' + dd + '日 是', get_week_day(day))
new = yy + '-' + mm + '-' + dd + '-' + day

str = 'output_' + re.sub('output_(.{10})', new, text)
print(str)