a = 10 # global variable
print(id(a))

def something():
    # global a
    a = 9

    # a = 15 # lokal variable

    x = globals()['a']
    print(id(x))
    print('in functin', a)

    globals()['a'] = 77



something()
print('outside', a)