# საკლასო დავალება:

# Task: Division Calculator with Error Handling

# Ask the user to input two numbers: a numerator and a denominator.

# Attempt to divide the numerator by the denominator inside a try block.

# If the user inputs something that is not a number, catch the error and display a message using except.

# If the user attempts to divide by zero, raise a ValueError with a custom message.

# Regardless of what happens, use a finally block to print a message like “Operation complete.”


User=int(input("Enter a numerator: "))
User1=int(input("Enter a denominator "))

try:
    print(User / User1)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    raise ValueError("Cannot divide by zero.")
finally:
    print("End of operations")