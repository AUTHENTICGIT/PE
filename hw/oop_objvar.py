class Robot:
    Population = 0

    def __init__(self, name):
        self.name = name
        print('(Initializing {})'.format(self.name))
        Robot.Population += 1

    def say_hi(self):
        print('Greetings, my masters call me {}.'.format(self.name))

    def die(self):
        print('{} is being destroyed!'.format(self.name))
        Robot.Population -= 1
        if Robot.Population == 0:
            print('{} was the last one.'.format(self.name))
        else:
            print('There are still {} robots working'.format(Robot.Population))

    @classmethod
    def how_many(cls):
        print('We have {} robots'.format(Robot.Population))

droid1 = Robot('R2-D2')
droid1.say_hi()
droid1.how_many()

droid2 = Robot('C-3PO')
droid2.say_hi()
droid2.how_many()

print('\nRobots can do some work here.\n')

droid1.die()
droid2.die()

Robot.how_many()