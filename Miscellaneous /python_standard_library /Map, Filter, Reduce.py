#MAP()
#map() applies a given function to each item of a sequence (list, tuple etc.) and returns a sequence of the results

def square(n):
   return n * n
numbers = [1, 2, 3, 4]
result = map(square, numbers)
numbers_square = list(result)
print(numbers_square)

#OUTPUT: [1, 4, 9, 16]

#Simplified version

numbers = list(map(int, input().split()))
print(numbers)


#OUTPUT: [1, 4, 9, 16]

#FILTER()
#filter() method filters the elements of a given sequence based on the result of given function.

def is_positive_number(num):
   return num > 0
  
list_a = [1, -2, 3, -4]
positive_nums = filter(is_positive_number, list_a)
print(list(positive_nums))

#OUTPUT: [1, 3]

#REDUCE()
#reduce() function is defined in the functools module.

from functools import reduce

def sum_of_num(a, b):
   return a+b

list_a = [1, 2, 3, 4]
sum_of_list = reduce(sum_of_num, list_a)
print(sum_of_list)

#OUTPUT: 10



