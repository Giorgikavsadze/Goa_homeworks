# 8) Find the Maximum
# Create a function that takes a list of numbers and uses a loop to find and return the maximum number.

def list_of_numbers(num_list):
    max_num=0
    for i in num_list:
        if i > max_num:
            max_num=i

    print(max_num)

list_of_numbers([1,2,3,4,5,6,7,9])