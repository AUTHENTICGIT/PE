# class Person:
#     # def __init__(self):
#     #     self.name = name
#
#     def say_hi(self, name):
#         print('Hello, my name is', name)
#
# p = Person()
# p.say_hi('Swaroop')

# 案例
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()