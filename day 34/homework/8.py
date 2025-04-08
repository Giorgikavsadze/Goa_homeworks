# 10) Write a function that iterates through a range of numbers (e.g., 1 to 100) and sums up all the numbers divisible by 3. Return the total sum.

def function (start,end):
    sum = 0
    for i in range(start,end+1):
        if i % 3 == 0:
            sum += i

    print(sum)

function(0,100)