#9) Write a program that takes two numbers and an operator (+, -, *, /) as input and performs the calculation. Display the result and end the program.

number = float(input("Enter number: "))
number1 = float(input("Enter number: "))
operators = input("Enter operators: ")


if operators == "+":
    result = number + number1
elif operators == "-":
    result = number - number1
elif operators == "*":
    result = number * number1
elif operators == "/":
    if number1 != 0:  
        result = number / number1
    else:
        result = "Division by zero is not allowed"  


print(result)
