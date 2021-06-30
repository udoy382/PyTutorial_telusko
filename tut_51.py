class Computer:
    def __init__(self):
        self.name = 'Udoy'
        self.age = 28

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c1.age = 30
c2 = Computer()

# print(id(c1))
# print(id(c2))

#       change class object
# c1.name = 'Maryam'
# c1.age = 11

if c1.compare(c2):
    print("They are same")
else:
    print("They are difference")

# c1.update()

print(c1.name)
print(c2.name)