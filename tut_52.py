class Car:
    #       types of variable or class variable
    vheels = 4

    def __init__(self):
        self.mil = 10
        self.com = 'BMW'

c1 = Car()
c2 = Car()

#       change object
c1.mil = 8
Car.vheels = 5

print(c1.com, c1.mil, c1.vheels)
print(c2.com, c2.mil, c2.vheels)