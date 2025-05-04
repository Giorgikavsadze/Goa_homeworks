# 1) თავიდან შეასრულეთ გაკვეთილზე შესრულებული ამოცანები:
# Exclusive "or" (xor) Logical Operator
def xor(a,b):
    if a!=b:
        return True
    else:
        return False
    

#What's the real floor?
def get_real_floor(n):
    if n<1:
        return n
    elif n<13:
        return n-1
    elif n > 13:
        return n-2
    

#Filter out the geese

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [i for i in birds if i not in geese ]


#Name Shuffler
def name_shuffler(s):
    parts = s.split()
    return f"{parts[1]} {parts[0]}"


#Find numbers which are divisible by given number
def divisible_by(numbers, divisor):
    return [i for i in numbers if i % divisor ==0]


#Lario and Muigi Pipe Problem

def pipe_fix(nums):
    return list(range(min(nums),max(nums)+1))



#Plural
def plural(n):
    return n == 0 or n>1


#Multiplication table for number
def multi_table(number):
    res = ""
    for i in range(1,11):
        res += f"{i} * {number} = {i*number}\n"
    return res[0:-1]

#Super Duper Easy
def problem(a):
    if type(a)==str:
        return "Error"
    return a*50+6
    
#Grasshopper - If/else syntax debug
def check_alive(health):
    if health > 0:
        return True
    else:
        return False
    

#Grasshopper - Basic Function Fixer
def add_five(num):
    total = num + 5
    return total

#Grasshopper - Terminal game combat function
def combat(health, damage):
    if health - damage > 0: return health - damage
    return 0

#საკლასო დავალება:

# https://www.codewars.com/kata/595970246c9b8fa0a8000086
#Capitalization and Mutability
def capitalize_word (word):
    return word[0].upper() + word[1:].lower()


#How many lightsabers do you own?
def how_many_light_sabers_do_you_own(*args):
    if len(args)==0:return 0
    return 18 if args[0] =="Zach" else 0


#საკლასო დავალება:

# https://www.codewars.com/kata/563b74ddd19a3ad462000054
#Stringy Strings
def stringy(size):
    res = ""
    
    for i in range(size):
        if i%2 == 0: res += "1"
        else: res += "0"

#Remove duplicates from list
def distinct(seq):
    res = []

    for i in seq:
        if i not in res: res.append(i)

    return res

#Merge two sorted arrays into one
def merge_arrays(arr1, arr2):
    merge = arr1 + arr2
    sort1 = sorted(set(merge))
    return sort1