# Ternary Operators
is_nice = True
state = "nice" if is_nice else "not nice"
print(state)

# ShortHand Ternary
True or "Some"
# Output: True
False or "Some"
# Output: 'Some'

output = None
msg = output or "No data returned"
print(msg)
# Output: No data returned

def my_function(real_name, optional_display_name=None):
    optional_display_name = optional_display_name or real_name
    print(optional_display_name)
my_function("John")
# Output: John
my_function("Mike", "anonymous123")
# Output: anonymous123