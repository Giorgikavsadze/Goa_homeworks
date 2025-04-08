#3) Write a program that takes three numbers as input and prints the largest of the three.

num=int(input("Enter number: "))
num1=int(input("Enter number: "))
num2=int(input("Enter number: "))


if num > num1 and num > num2:
    print(num)
elif num1 > num and num1>num2:
    print(num1)
else:
    print(num2)







