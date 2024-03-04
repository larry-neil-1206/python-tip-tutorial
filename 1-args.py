'''
Code example for normal arguments, *args and **kwargs
FYI, it can be used when making function decorators and monkey patching.
monkey patching means modifying or extending the code at runtime.
'''
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)


test_var_args("yasoob", "python", "eggs", "test")

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))
        
greet_me(name="yasoob")

args = ("two", 3, 5)
test_var_args(*args)
kwargs = {"three": 3, "five": 5}
greet_me(**kwargs)