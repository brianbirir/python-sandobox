class Animal:

    def __init__(self, name):

        self.name = name

    def eat(self, food):

        print('{} is eating {}.'.format(self.name, food))


class Dog(Animal):

    def fetch(self, thing):

        print('{} goes after the {}.'.format(self.name, thing))

    def show_affection(self):

        print('{} wags tails.'.format(self.name))


class Cat(Animal):

    def swatstring(self):

        print('{} shreds the string.'.format(self.name))

    def show_affection(self):

        print('{} purrs.'.format(self.name))


# inheritance test
r = Dog('Rover')

f = Cat('Fluffy')

r.fetch('paper')
f.swatstring()
r.eat('dog food')

# polymorphism test
for a in (Dog('Rover'), Cat('Fluffy'), Cat('Precious'), Dog('Scout')):

    a.show_affection()
