# საკლასო დავალება:

# Write a function apply_to_list(func, values) that takes a function func and a list values, and returns a new list where func is applied to each element.

# Then:

# Define a function square(x) that returns the square of a number.


def square(num):
    return num**2
def apply_to_list(func,user_list):
    new_list=[]

    for i in user_list:
        new_list.append(func(i))

    return new_list

print(apply_to_list(square, list(range(10))))