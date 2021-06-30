'''
there are 3 types of method
- Instance methods
- Class methods
- Static methods

'''

class Student():

    school = 'Telusko'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    # def get_m1(self):
    #     return self.m1
    
    # def get_m1(self, value):
    #     self.m1 = value

#       class methods use when work with class variavle or methods like cls
    @classmethod
    def getSchool(cls):
        return cls.school

#       static method use when cannot use any class or self method 
    @staticmethod
    def info():
        print("This is Studen class... this is static method no cls, no self")

s1 = Student(34, 54, 65)
s2 = Student(45, 65, 25)

print(s1.avg())
print(Student.getSchool())
print(Student.info())