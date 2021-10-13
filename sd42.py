class Dog(object):
    def __init__(self):
        self.name = "Doge"
        self.__money = 10000000

    def hi(self):
        print(self.name)

    def bye(self):
        print(self.__money)

a = Dog()
a.hi()
a.bye()

class Poodle(Dog):
    def __init__(self, money):
        super().__init__()
        self.__money = money

    def bye(self):
        print(self.__money)

b = Poodle(1)
b.hi()
b.bye()
