x = int(input('Enter an integer:'))
if(x == 23):
    print('''Congratulations, you guessed it.
(but you do not win any prizes!)''')
elif(x > 23):
    print('No, it is a little lower than that')
else:
    print('No, it is a little higher than that')
print('Done')

# 案例
number = 23
guess = int(input('Enter an integer:'))

if guess == number:
    # 新块从这里开始
    print('Congratulations, you guessed it.')
    print('but you do not win any prizes!')
    # 新块在这里结束
elif guess < number:
    # 新块从这里开始
    print('No, it is a little higher than that')
    # 新块在这里结束
else:
    print('No, it is a little lower than that')
    # 你必须通过猜测一个大于（>）设置数的数字来到达这里。

print('Done')
# 这最后一句语句将在
# if语句执行完毕后执行
