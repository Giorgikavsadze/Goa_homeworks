#5) Write a program that takes a number as input and prints whether it is positive, negative, or zero.

num=int(input("Enter number: "))

if num > 0:
    print("positive")
elif num < 0:
    print("negative")
elif num == 0:
    print("zero")
else:
    print("incorrect number")