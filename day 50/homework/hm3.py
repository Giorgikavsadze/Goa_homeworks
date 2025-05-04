# 3)Try adding an integer to a string and catch the TypeError.

try:
    sum_of_int_and_str=5+"4"
except TypeError:
    print("you can't sum up int and string ")