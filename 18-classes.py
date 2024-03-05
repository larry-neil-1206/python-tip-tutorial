"""
Instance & Class variables

The basic difference is:

Instance variables are for data which is unique to every object
Class variables are for data shared between different instances of a class

Class magic methods, commonly called dunder (double underscore) methods.
"""

class Cal(object):
    # pi is a class variable
    pi = 3.142

    def __init__(self, radius):
        print('Cal executed {0}'.format(radius))
        # self.radius is an instance variable
        self.radius = radius

    def __getitem__(self, key):
        print('===> __getitem__ executed {0}*{1}'.format(key, self.pi))
        return self.pi*key
      
    def area(self):
        return self.pi * (self.radius ** 2)

a = Cal(32)
a.area()
# Output: 3217.408
a.pi = 43
# Output: 43

b = Cal(44)
b.area()
# Output: 6082.912
b.pi = 50
# Output: 50

print(a[3])
print(b[3])

class SuperClass(object):
    superpowers = []

    def __init__(self, name):
        self.name = name

    def add_superpower(self, power):
        self.superpowers.append(power)

foo = SuperClass('foo')
bar = SuperClass('bar')
foo.name
# Output: 'foo'

bar.name
# Output: 'bar'

foo.add_superpower('fly')
bar.superpowers.append('cry')
# Output: ['fly']

foo.superpowers
# Output: ['fly']