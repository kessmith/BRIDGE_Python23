import random

"""
Python Expressions Example
"""
num_items = 2
# num_items = num_items + 2
num_items += 2
print(num_items)


print('*************************************************************************************************************************************')
"""
Pseudo-random
"""
# Generates a unique seed
random.seed(10)
# random.seed(15) # Show the students that even though we change the seed and then change it back the value stays the same

# Geenrate a random integer between 1, 10
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))