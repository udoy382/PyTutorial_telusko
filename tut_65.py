f = open("MyData", "r")

# print(f.read())
# print(f.readline(), end="")

#-------------------------------------

f1 = open('abc', 'w')

# f1.write("Something")
# f1.write(" People")
# f1.write("Laptop")

#--------------------

f2 = open('abc', 'a')

# f2.write("Mobile")
# f2.write(" Laptop")

#-------------------------
# for data in f:
#     # print(data)
#     f1.write(data)

#----------------------
#       rb means read binary and wb means write binary
#       how to copy image

f = open("1.jpg", "rb")
f1 = open('MyPic.JPG', 'wb')

for i in f:
    # print(i)
    f1.write(i)