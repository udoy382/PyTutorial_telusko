class A:
    def future1(self):
        print('Feature 1 working')


    def future2(self):
        print('Feature 2 working')

# class B(A):
class B():
    def future3(self):
        print('Feature 3 working')


    def future4(self):
        print('Feature 4 working')

# class C(B):
class C(A, B):
    def future5(self):
        print('Feature 5 working')

'''
    There are 3 type of inheritance
single inheritance
multilevel inheritance
multipul inheritance

'''
a1 = A()

a1.future1()
a1.future2()

b1 = B()

# b1.future1()
# b1.future4()

c1 = C()

c1.future5()