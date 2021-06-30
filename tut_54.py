class Student:
    def __init__(self, name, roolno):
        self.name = name
        self.roolno = roolno
        self.laptop = self.Laptop()

    def show(self):
        print(self.name, self.roolno)

#       class inside a class or inner class
    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i3'
            self.ram = 4

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student('Udoy', 2)
s2 = Student('Maryam', 3)

print(s1.name, s1.roolno)
print(s2.name, s2.roolno)

# s1.show()

lap1 = s1.laptop
lap2 = s2.laptop

# print(id(lap1))
# print(id(lap2))

lp1 = Student.Laptop()
lap1.show()
lap2.show()