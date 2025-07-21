# 1) თავიდან შეასრულეთ გაკვეთილზე ამოხსნილი ამოცანები:

# Sum of the first nth term of Series
def series_sum(n):
    if n == 0:
        return "0.00"
    total = 0
    for i in range(n):
        total += 1 / (1 + 3 * i)
    return f"{total:.2f}"
    

#Find the divisors!
def divisors(integer):
    result = [i for i in range(2, integer) if integer % i == 0]
    if result:
        return result
    else:
        return f"{integer} is prime"

#Remove the minimum
def remove_smallest(numbers):
    if not numbers:
        return []

    min_index = numbers.index(min(numbers)) 
    return numbers[:min_index] + numbers[min_index + 1:]

#Testing 1-2-3
def number(lines):
    return [f"{i + 1}: {line}" for i, line in enumerate(lines)]

#Count the divisors of a number
def divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count += 1 if i * i == n else 2 
    return count

# 2-6) შეასრულეთ ამოცანები:

#Find the stray number
def stray(arr):
    for num in arr:
        if arr.count(num) == 1:
            return num
        

#Sort Numbers
def solution(nums):
    if not nums: 
        return []
    else:
        return sorted(nums)
    
#Make a function that does arithmetic!
def arithmetic(a, b, operator):
    if operator == "add":
        return a+b
    elif operator == "subtract":
        return a-b
    elif operator == "multiply":
        return a*b
    elif operator == "divide":
        return a/b
    
#Breaking chocolate problem
def break_chocolate(n, m):
    if n == 0 or m == 0:
        return 0
    return n * m - 1

#Anagram Detection
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())