import os
import time

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

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')