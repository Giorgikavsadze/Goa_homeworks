# Use map() to check if numbers in a list are greater than 50.

list1=[1,200,3,45,50,6,7,85,90,50]
greater=lambda num:num>50
print(list(map(greater,list1)))