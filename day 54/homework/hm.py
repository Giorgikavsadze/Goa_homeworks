# User Input Number Division
# Ask the user to enter two numbers and divide them. Handle errors like division by zero and non-numeric input.



try:
    User=int(input("Enter number: "))
    User1=int(input("Enter number: "))
    print(User/User1)
except ZeroDivisionError:
    print("your second number can't be zero")
except ValueError:
    print("you can't input non-numeric input")
