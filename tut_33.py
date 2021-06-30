def update(x):

    # print(id(x))
    print(id(lst))

    # x = 8
    lst[1] = 25
    # print(id(x))
    print(id(lst))
    # print('x ', x)
    print('x ', lst)


# a = 10
lst = [10, 20, 30]
# print(id(a))
print(id(lst))
# update(a)
update(lst)
# print('a ', a)
print('a ', lst)