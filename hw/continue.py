while True:
    s = input('Enter something:')
    if s == 'quit':
        break
    if len(s) < 3:
        print('too small')
        continue
    print('Input is of sufficient length')

# 案例 同上
