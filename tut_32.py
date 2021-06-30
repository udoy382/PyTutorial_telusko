def greet():
    print("Hello")
    print("Good morning")

# greet()
# greet()

#------------------------

def add(x, y):
    c = x + y
    d = x-y
    # print(c)
    return c, d

result1, result2 = add(5, 4)
print(result1, result2)