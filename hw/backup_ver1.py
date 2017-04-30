import time
import os

# 1.需要备份的文件和目录将被
# 指定在一个列表中
source = '/Users/learnlearn/Pictures/imagePNG'
# 在这里注意到我们必须在字符串中使用双引号
# 用以括起其中包括空格的名称。
# 2.备份文件必须存储在一个
# 主备份目录中
target_dir = '/Users/learnlearn/Pictures/Backup'

# 3.备份文件将被打包压缩成zip文件
# 4.zip压缩文件的文件名由当前日期与时间构成
target = target_dir + os.sep + \
time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5.使用zip命令将文件打包成zip格式
zip_command = 'zip -r {0}{1}'.format(target, ''.join(source))

# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
