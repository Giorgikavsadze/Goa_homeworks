# Convert String to Integer
# Ask the user for a number and convert it to an integer. Handle the error if they enter something that can't be converted.


try:
    User=int(input("Enter number: "))
    print(User)
except ValueError:
    print("you should enter integer")

    

