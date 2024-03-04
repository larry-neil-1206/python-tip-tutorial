"""
An [iterable] is any object in Python which has an [__iter__] or a [__getitem__] method defined which returns an iterator or can take indexes
An [iterator] is any object in Python which has a [next] (Python2) or [__next__] method defined. 
"""

# def generator_function():
#     for i in range(10):
#         yield i

# for item in generator_function():
#     print(item)
    
# def fibon(n):
#     a = b = 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
        
# for x in fibon(10):
#     print(x)
    
# def generator_function():
#     for i in range(3):
#         yield i

# gen = generator_function()
# print(next(gen))
# # Output: 0
# print(next(gen))
# # Output: 1
# print(next(gen))
# # Output: 2
# print(next(gen))

# my_string = "Yasoob"
# my_iter = iter(my_string)
# print(next(my_iter))