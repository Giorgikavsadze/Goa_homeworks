#2) Sum of Two Numbers: Write a function that takes two numbers as input and returns their sum.

def sum (num1,num2):
    print(num1+num2)

sum(4,3)
sum(9,5)


#3) Even or Odd: Create a function that determines whether a given integer is even or odd.

def evenorodd(num):
    if num  % 2 == 0:
        print("number is even")
    else:
        print("number is odd")

evenorodd(0)
evenorodd(4)
evenorodd(9)
evenorodd(13)


# 4) Reverse a String: Implement a function that takes a string and returns it reversed.
# გამოიყენეთ slicing

def reverse(string):
    print(string[::-1])

reverse("computer")

#5) Find Maximum: Create a function that takes a list of numbers and returns the maximum value.

def find_max(num, num1, num2, num3):
    
    max_num = num

    
    if num1 > max_num:
        max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3

    
    print(max_num)



find_max(1,2,3,4)



# 6) Factorial: Implement a function to calculate the factorial of a given number.

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    print(result) 


factorial(4)  
factorial(5)