my_list = ['apple', 'banana', 'grapes', 'pear']
for counter, value in enumerate(my_list, 2):
    print (counter, value)
    
my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)
# Output: [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]