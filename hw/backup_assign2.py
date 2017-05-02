import sys
import os
import time

print('The command line arguments are:')
print(sys.argv)

source = ['/Users/learnlearn/PycharmProjects/pe/hw',]
target_dir = '/Users/learnlearn/Documents/Backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
time = time.strftime('%H%M%S')

comment = input('Enter a comment --->')
if len(comment) == 0:
    target = today + os.sep + time + '.zip'
else:
    target = today + os.sep + time + '_' + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)

# 是否有额外的文件或目录传递到脚本
if len(sys.argv) > 0:
    for path in sys.argv[1:]:
        source.append(path)

zip_command = 'Zip -r {0} {1}'.format(target, ' '.join(source))

print('Zip command is:')
print(zip_command)
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')