# list comprehensions provide a short and concise way to create lists. 
# It consists of square brackets containing an expression followed by a for clause, then zero or more for or if clauses. 
# blueprint: variable = [out_exp for out_exp in input_list if out_exp == 2]

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)
# Output: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

# general way to create a list
squared = []
for x in range(10):
    squared.append(x**2)
    
# list comprehension way to create a list
squared = [x**2 for x in range(10)]

# set comprehension
squared = {x**2 for x in [1, 1, 2]}
print(squared)
# Output: {1, 4}

# generator comprehension
multiples_gen = (i for i in range(30) if i % 3 == 0)
print(multiples_gen)
# Output: <generator object <genexpr> at 0x7fdaa8e407d8>
for x in multiples_gen:
  print(x)