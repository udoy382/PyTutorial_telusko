#       filter function
'''
# def is_even(n):
#     return n%2==0

#       user functions or lambda for filter the nums value lambda is a sort functions

# x = lambda p : p%2==0

nums = [2, 3, 5, 7, 5, 9, 6, 3, 6, 4, 9, 8]

# events = list(filter(x, nums))
events = list(filter(lambda n: n%2==0, nums))

print(events)
'''

#       map function
'''
# def update(n):
#     return n+2

#       use def function or lambda function lambda is a sort function

nums = [2, 3, 6, 8, 9, 6, 7, 4, 8, 5, 9]

events = list(filter(lambda n: n%2==0, nums))
# print(events)

# doubles = list(map(update, events))
doubles = list(map(lambda n: n+2, events))
print(doubles)
'''
#       reduce function

from functools import reduce

# def add_all(a,b):
#     return a+b

nums = [2, 3, 6, 8, 9, 6, 7, 4, 8, 5, 9]

events = list(filter(lambda n: n%2==0, nums))

doubles = list(map(lambda n: n+2, events))

# sum = reduce(add_all, doubles)
sum = reduce(lambda a,b : a+b, doubles)
print(sum)