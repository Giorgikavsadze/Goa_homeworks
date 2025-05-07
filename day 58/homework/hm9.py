# Use map() to convert a list of integers to strings.

list1=[1,2,3,4,5,6,7,8,9,10]
turn_into_string=lambda string:str(string)
print(list(map(turn_into_string,list1)))