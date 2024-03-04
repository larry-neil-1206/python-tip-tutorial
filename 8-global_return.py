from collections import namedtuple
def profile():
    Person = namedtuple('Person', 'name age')
    return Person(name="Danny", age=31)

# Use as namedtuple
p = profile()
print(p, type(p))
# Person(name='Danny', age=31) <class '__main__.Person'>
print(p.name)
# Danny
print(p.age)
#31

# Use as plain tuple
print(p[0])
# Danny
print(p[1])
#31

# Unpack it immediatly
name, age = p
print(name)
# Danny
print(age)
#31

def add(value1, value2):
    return value1 + value2

result = add(1, 2)
print(result)
# Output: 3

def add(value1,value2):
    global result
    result = value1 + value2

add(3,5)
print(result)
# Output: 8