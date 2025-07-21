# Sum of odd numbers
def row_sum_odd_numbers(n):
    return n ** 3

#Printer Errors
def printer_error(s):
    count = 0
    AtoM = "abcdefghijklm"
    for i in s:
        if i not in AtoM:
            count += 1
    return f"{count}/{len(s)}"

#Reverse words
def reverse_words(text):
    return ' '.join(i[::-1] for i in text.split(' '))

#Ones and Zeros
def binary_array_to_number(arr):
    return int(''.join(str(i) for i in arr),2)

#Number of People in the Bus
def number(bus_stops):
    people_on_bus = 0
    for on, off in bus_stops:
        people_on_bus += on
        people_on_bus -= off
    return people_on_bus
    

#Odd or Even?
def odd_or_even(arr):
    sum_of_nums=sum(arr)
    if sum_of_nums%2==0:
        return "even"
    else:
        return "odd"
    
#The highest profit wins!
def min_max(lst):
    return [min(lst),max(lst)]