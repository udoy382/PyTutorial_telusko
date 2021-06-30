
def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    
    return even , odd


lst = [1, 2, 3, 45, 87, 56, 87, 56, 87, 66, 56, 45, 77, 67]
even, odd = count(lst)

print("Even : {} and odd : {}".format(even, odd))