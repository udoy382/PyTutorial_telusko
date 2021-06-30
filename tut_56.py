class A:

    def __init__(self):
        print("in A init")

    def future1(self):
        print('Feature 1-A working')


    def future2(self):
        print('Feature 2 working')

# class B(A):
class B:
    def __init__(self):
        #       super().__init__() is use for print super class method 
        # super().__init__()
        print("in B init")

    def future1(self):
        print('Feature 1-B working')


    def future4(self):
        print('Feature 4 working')

class C(A, B):
    def __init__(self):
        super().__init__()
        print("in C init")

    def feat(self):
        super().future2()

# a1 = B()
a1 = C()
a1.future1()
a1.feat()