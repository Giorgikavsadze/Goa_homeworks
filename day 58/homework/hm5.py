# Use map() to add 10 to every number in a list.

list1=[1,2,3,4,5,6,7,8,9,10]
adds_ten=lambda num:num+10
print(list(map(adds_ten,list1)))