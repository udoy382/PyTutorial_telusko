class Computer:
    def config(self):
        print("i3, 4gb, 1tb")



com1 = Computer()
com2 = Computer()
# print(type(com1))

Computer.config(com1)
Computer.config(com2)


com1.config()
com2.config()