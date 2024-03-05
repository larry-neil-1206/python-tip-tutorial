my_list = [1, 2, 3, 7, 4]
print(dir(my_list))
my_list = my_list.__add__([14, 15, 16])
my_list.insert(2, 17)
print(my_list)

print(type(''))
# Output: <type 'str'>

print(type([]))
# Output: <type 'list'>

print(type({}))
# Output: <type 'dict'>

print(type(dict))
# Output: <type 'type'>

print(type(3))
# Output: <type 'int'>

name = "Yasoob"
print(id(name))
# Output: 1650198468784

import inspect
print(inspect.getmembers(str))
# Output: [('__add__', <slot wrapper '__add__' of ... ...