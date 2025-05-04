# 1)Prompt the user to enter a number. If the input is not a number, display an error message.


try:
    User=int(input("Enter number: "))
except ValueError:
    print("not integer")
