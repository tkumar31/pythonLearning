
try:
    #div = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Invalid Number!")

