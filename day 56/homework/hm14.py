# 16) Check if the user is tall enough
# Task: Ask the user for their height (in cm) and check if they are taller than 150 cm. Print an appropriate message based on their height.

user=float(input("Enter your height in cm: "))
if user > 1.50:
    print( "you are taller than 1.50cm")
elif user < 1.50:
    print("you are shorter than 1.50cm")
else:
    print("you are exactly 1.50 cm")
