'''
def add(a, b): # when im use argumets on function like a , b, or more it is "Formal Arguments"
    c = a + b
    print(c)

add(5, 6) # when im call function, in this time what argumets im input it is "actual Arguments"
'''

'''

total arguments is 4 types
~ Position
~ Keyword
~ Default
~ Variable Length

'''

#       Positional Arguments
'''
def person(name,age):
    print(name)
    print(age-5)

person('Udoy', 17)
# person(17, 'udoy') # this is not positional arguments
'''

#       Keyword Arguments
'''
def person(name,age):
    print(name)
    print(age-5)

person(age=17, name='udoy')
'''

#       Default Arguments
'''
def person(name,age=17):
    print(name)
    print(age)

person('udoy', 28) # there is default arguments age, 28
'''

#       Variable Length Arguments
#       a is first value like ' 5 ' and b is last all value like ' 6, 34, 78 ' or more cause it is variable length arguments
#       first we give * for second or more value in function arguments a is int object and b is tuple object
#       if we sum a or b we user for loop cause a is int and b is tuple

def sum(a, *b):
    # print(a)
    # print(b)

    # c = 0 # if we can't give ' a ' in function aguments so we use c = 0
    c = a
    for i in b:
        c = c + i
    
    print(c)

sum(5, 6, 34, 78)