# 7) Write a function that takes a list of numbers and checks whether each number is even or odd using a loop and conditional statements. Print "Even" for even numbers and "Odd" for odd numbers.

def list_of_numbers(num_list):
    for i in num_list:
        if i % 2 == 0:
            print("even")
        else:
            print("odd")

list_of_numbers([1,2,3,4,5,6])