# 5) თავიდან შეასრულეთ გაკვეთილზე შესრულებული ამოცანები: 

# https://www.codewars.com/kata/52fba66badcd10859f00097e
# https://www.codewars.com/kata/546e2562b03326a88e000020
# https://www.codewars.com/kata/554b4ac871d6813a03000035
# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
# https://www.codewars.com/kata/5467e4d82edf8bbf40000155


# Disemvowel Trolls
def disemvowel(string):
    vowels = "aeiouAEIOU"
    res = ""

    for i in string:
        if i not in vowels:
            res += i

    return res


#Square Every Digit 

def square_digits(num):
    st = []

    for i in str(num):
        int_i = int(i)
        sq_i = int_i**2
        st.append(str(sq_i))

    return int("".join(st))

#Highest and Lowest

def high_and_low(numbers):
    nums = list(map(int, numbers.split()))
    return f"{max(nums)} {min(nums)}"


#List Filtering

def filter_list(l):
    return [i for i in l if type(i) == int]

#Descending Order
def descending_order(num):
    digits = list(str(num))
    for i in range(len(digits)):
        max_idx = i
        for j in range(i + 1, len(digits)):
            if digits[j] > digits[max_idx]:
                max_idx = j
        digits[i], digits[max_idx] = digits[max_idx], digits[i]
    return int(''.join(digits))


#You're a square!  
def is_square(n):    
    if n < 0:
        return False
    x = int(n ** 0.5)
    return x * x == n
