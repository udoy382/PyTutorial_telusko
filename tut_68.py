# How to search number, Linear search using python

pos = -1

def search(list, n):
    i = 0
    while i< len(list):
        if list[i] == n:
            # pos = i
            globals()['pos'] = i
            return True
        i+=1

    return False


list = [5, 8, 6, 9, 2]
n = 9

if search(list, n):
    print(f"Found at {n} position is > ", pos+1)
else:
    print(f"Not Found {n}")