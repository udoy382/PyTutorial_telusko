#       break statment
'''
x = int(input("How many candies you want: "))

av = 6

i = 1
while i <=x:
    if i>av:
        print("Out of stock")
        break

    print("Candy")
    i+=1

print("Bye")
'''

#       continue statment
'''
for i in range(1, 101):
    if i%3==0 or i%5==0:
        continue
    print(i)

print("Bye")
'''

#       pass statment
for i in range(1, 101):
    
    if i%2!=0:
        pass

    else:
        print(i)

print("Bye")