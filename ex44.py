class Mammal(object):

    def __init__(self):
        print "init mammal"

    def breath(self):
        print "Suuu Haahh"

class Dog(Mammal):

    def __init__(self):
        super(Dog, self).__init__()
        print "init dog"

    def breath(self):
        super(Dog, self).breath()
        print "Bruuuuuh"

pochi = Dog()
big = Mammal()

pochi.breath()
big.breath()