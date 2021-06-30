
a = 5
b = 2

try:
    print("Resource open")
    print(a/b)

    k = int(input("Enter a number: "))
    print(k)

# except Exception as e:
except ZeroDivisionError as e:
    print("Hey you cannot divide a number by zero", e)

except ValueError as e:
    print("Invalid input")

except Exception as e:
    print("Something want wrong...")

finally:
    print("Resource close")

print("bye")