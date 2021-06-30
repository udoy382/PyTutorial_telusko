'''
a = 5
b = 'world'
c = 6

d = '5'
e = '9'

print(d + e)
print(int.__add__(d,e))
'''

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

#       add two student ( s1 or s2 ) marks add
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

#       compare student marks whos marks is high
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        # return self.m1, self.m2
        return f"{self.m1} {self.m2}"

s1 = Student(50, 69)
s2 = Student(60, 65)

s3 = s1 + s2

# print(s3.m2)

#       compare student marks whos marks is high
if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")


a = 9
print(a.__str__())
# print(s1.__str__())
print(s1)
print(s2)