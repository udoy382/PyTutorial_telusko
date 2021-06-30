#       if im give one ' * ' in data so it does not work cause im user keyword arguments in calling function
#       if im give two ' ** ' in function so it print all method with keyword arguments

def person(name, **data):
    print(name)
    # print(data)

    for key, value in data.items():
        print(key, value)

person('udoy', age=17, city='sylhet', mob=123456)