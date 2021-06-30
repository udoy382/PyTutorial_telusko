from array import *

arr = array('i',[])

n = int(input("Enter the length of the array: "))

for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)


print(arr)

val = int(input("Enter the value for search: "))

#       search value in arary with own method, first way to pint
# k = 0
# for e in arr:
#     if e==val:
#         print(k)
    
#     k+=1h

#       search value in array with function, second way to print
print(arr.index(val))