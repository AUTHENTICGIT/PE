import os
import time

# 指定需要备份的文件和目录在一个列表中
source = ['/Users/learnlearn/PycharmProjects/pe/hw', '/Users/learnlearn/PycharmProjects/pc']
# 备份文件存储在一个主备份目录
target_dir = '/Users/learnlearn/Documents/Backup'

# 如果主备份目录不存在则创建目录
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 将当前日期作为主备份目录下的子目录名称
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 将当前时间作为zip文件的文件名
time = time.strftime('%H%M%S')

# zip文件名称格式
target = today + os.sep + time + '.zip'

# 检查是否存在子目录文件夹，没有则新建一个
if not os.path.exists(today):
    os.mkdir(today)

# 使用zip命令将文件打包成zip格式
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')