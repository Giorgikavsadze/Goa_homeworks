# Use filter() to get numbers divisible by 3 from a list.

divisible=list(filter(lambda num:num%3==0 ,[1,20,3,4,52,60,7,8,9,10]))
print(divisible)