# Lambdas are one line functions.

add = lambda x, y: x + y

print(add(3, 5))
# Output: 8

a = [(1, 2), (4, 1), (9, 10), (13, -3)]
# a.sort(key=lambda x: x[1])

def get_second_element(x):
    return x[1]

a.sort(key=get_second_element)

print(a)
# Output: [(13, -3), (4, 1), (1, 2), (9, 10)]