import os
import time
import zipfile

# source = '/Users/learnlearn/PycharmProjects/pe/hw/'
source = ['/Users/learnlearn/PycharmProjects/pe/hw', '/Users/learnlearn/PycharmProjects/pc']
target_dir = '/Users/learnlearn/Documents/Backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
time = time.strftime('%H%M%S')

comment = input('Enter a comment --> ')
# 检查是否有评论键入
if len(comment) == 0:
    target = today + os.sep + time + '.zip'
else:
    target = today + os.sep + time + '_' + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)

# 运行备份
print('Running:')
# 使用zipfile模块将文件打包成zip格式
# 注意这里的第二个参数是'w'，这里的target是压缩包的名字，这里的ZIP_DEFLATED是压缩模式
z = zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED)
try:
    for path in source:
        for file in os.listdir(path):
            z.write(path + os.sep + file)
            print('  adding:', path + os.sep + file)
    # close()必须调用
    z.close()
    print('Successful backup to', target)
except:
    print('Backup FAILED')