#Randomness is useful in whenever uncertainty is required.  
#For example: Rolling a dice, flipping a coin, etc., 
#random  module provides us utilities to create randomness.

#randint() is a function in random module which returns a random integer in the given interval.

import random
random_integer = random.randint(1, 10)
print(random_integer)

#output: 8

#choice() is a function in random module which returns a random element from the sequence. 

import random
random_ele = random.choice(["A","B","C"])
print(random_ele)

#To know more about Python Standard Library, go through the authentic python documentation 
#https://docs.python.org/3/library/
