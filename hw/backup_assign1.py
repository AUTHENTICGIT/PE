import os
import time
import zipfile

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
z = zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED)

verbosity = input('''The default action is to show normal details, which can include the special name - to compress standard input.
-v  variety: execution with more information
-q  quiet: quiet execution with no details
Please enter a verbosity -->''')
# 检查是否有执行参数键入
try:
    for path in source:
        for file in os.listdir(path):
            z.write(path + os.sep + file)
            if verbosity == '-v':
                print('  adding:', path + os.sep + file)
    # close()必须调用
    z.close()
    print('Successful backup to', target)
except:
    print('Backup FAILED')