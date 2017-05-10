# 通常判断原字符串与倒序字符串相等
# 但 倒序 与 比较 拆分开执行
# def reverse(text):
#     return text[::-1]
#
# def is_palindrome(text):
#     return text == reverse(text)
#
# something = input('Enter text: ')
# if is_palindrome(something):
#     print('Yes, it is a palindrome')
# else:
#     print('No, it is not a palindrome')

# 作业练习：忽略标点、空格和大小，比如“Rise to vote, sir.”文本
def reverse(text):
    return ignore(text)[::-1]

def is_palindrome(text):
    return text == reverse(text)

def ignore(text):
    forbidden = (".", "?", "!", ":", ";", "-", "—", "(", ")", "[", "]", "...", "’", "“", "”", "/", ",", " ")
    str = ''
    for char in text:
        if char in forbidden:
            char = ''
        str = str + char
    return str

something = input('Enter text: ')
if is_palindrome(ignore(something)):
    print('Yes, it is a palindrome')
else:
    print('No, it is not a palindrome')
