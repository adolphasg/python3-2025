# import libraries
# 1. random – Generate random numbers
import random
print("Random number between 0 and 10:", random.randint(0, 10))

# 2. datetime – Get the current date and time
import datetime
now = datetime.datetime.now()
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

# 3. os – Interact with the operating system
import os
print("Current working directory:", os.getcwd())
print("List of files:", os.listdir())

# 4. collections – Count items using Counter
from collections import Counter
sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counts = Counter(sample_list)
print("Item counts:", counts)

# 5. itertools – Generate combinations
import itertools
print("Combinations of ['a', 'b', 'c'] taken 2 at a time:")
for combo in itertools.combinations(['a', 'b', 'c'], 2):
    print(combo)
