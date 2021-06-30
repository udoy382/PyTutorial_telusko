from numpy import *

'''
arr1 = array([1, 2, 3, 4, 5])
arr2 = array([6, 1, 9, 3, 2])
# arr = arr1 + 5

arr3 = arr1 + arr2

# print(arr)

print(arr3)
'''

#       some methos here
'''
arr1 = array([1, 2, 3, 4, 5])
arr2 = array([6, 1, 9, 3, 2])

# print(sin(arr1))
# print(cos(arr1))
# print(log(arr1))
# print(sqrt(arr1))
# print(sum(arr1))
# print(min(arr1))
# print(max(arr1))
print(concatenate([arr1, arr2]))
'''

arr1 = array([2, 6, 8, 1, 3])

# arr2 = arr1.view() # if im user .view() so it is exject copyed, and change id address. it is Shallow copy
arr2 = arr1.copy() # if im user .copy() so it is exject copyed, and change id address. it is Deep copy

arr1[1] = 7

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))