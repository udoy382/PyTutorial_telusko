#       Generator

def topten():

    # yield 1
    # yield 2
    # yield 3
    # yield 4

    n = 1
    while n<=10:
        sq = n*n
        yield sq
        n+=1

value = topten()

print(value.__next__())
print(value.__next__())
print(value.__next__())


for i in value:
    print(i)