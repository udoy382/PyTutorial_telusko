# this is array table, we only use this table to print array value, we user TypeCode when work or print array

'''

TypeCode    C Type      Python Type     Min.size in bytes
_____________________________________________________________

  'b' ---- signed char ----- int ----------------- 1
  'B' ---- unsigned char --- int ----------------- 1
  'u' ---- Py_UNICODE ----- unicode character ---- 2
  'h' ---- signed short ---- int ----------------- 2
  'H' ---- unsigned short ---- int --------------- 2
  'i' ---- signed int ------- int ---------------- 2
  'I' ---- unsigned int ----- int ---------------- 2
  'I' ---- signed long ------ int ---------------- 4
  'L' ---- unsigned long ---- int ---------------- 4
  'f' ---- float ------------ float -------------- 4
  'd' ---- double ----------- float -------------- 8

'''

from array import *

vals = array('i',[5, 9, 8, 4, 2])

# vals = array('u',['a', 'e', 'i'])

# print(vals.buffer_info())
# vals.reverse()
# print(vals[0])

# for i in range(5):
#     print(vals[i])

# for i in range(len(vals)):
#     print(vals[i])

# for e in vals:
#     print(e)

#       print caruactor second vals

# vals.reverse()
# print(vals)

# for i in range(3):
#     print(vals[i])


# --------------

newArr = array(vals.typecode, (a for a in vals))

# print(newArr)

# for e in newArr:
#     print(e)

i = 0

while i<len(newArr):
    print(newArr[i])
    i+=1