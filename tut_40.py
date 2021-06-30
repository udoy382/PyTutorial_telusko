
#       sys use for incrise recursion , recursion is default print 100 we incrise 2000 time
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

i = 0

def greet():
    global i
    i+=1
    print("Hello", i)
    greet()

greet()