# 1) თავიდან შეასრულეთ გაკვეთილზე შესრულებული ამოცანები:

# Alternate capitalization
def capitalize(s):
    even_caps = ""
    odd_caps = ""
    
    for i in range(len(s)):
        if i % 2 == 0: 
            even_caps += s[i].upper()
            odd_caps += s[i].lower()
        else: 
            even_caps += s[i].lower()
            odd_caps += s[i].upper()
    
    return [even_caps, odd_caps]


#No oddities here
def no_odds(values):
    result = []
    for i in values:
        if i % 2==0:
            result.append(i)
    return result
    

#Check the exam
def check_exam(arr1, arr2):
    result = 0
    for i in range(len(arr1)):
        if arr2[i] == "":         
            result += 0
        elif arr2[i] == arr1[i]: 
            result += 4
        else:                    
            result -= 1
    return result if result > 0 else 0


#Fix string case
def solve(s):
    
    lower = sum(1 for i in s if i.islower())
    upper = sum(1 for i in s if i.isupper())
    
    
    if upper > lower:
        return s.upper()
    else:
        return s.lower()
    
#Number of Decimal Digits
def digits(n):
    s = str(n)
    if s[0] == '':
        s = s[1:]
    return len(s)

#2-6)
# The Coupon Code
# ??


#Are the numbers in order?
def in_asc_order(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

#Flatten and sort an array
def flatten_and_sort(array):
    flat = [i for t in array for i in t] 
    return sorted(flat)                           


#Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

#Maximum Length Difference
def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1
    max_a1 = max(len(s) for s in a1)
    min_a1 = min(len(s) for s in a1)
    max_a2 = max(len(s) for s in a2)
    min_a2 = min(len(s) for s in a2)
    return max(abs(max_a1 - min_a2), abs(max_a2 - min_a1))