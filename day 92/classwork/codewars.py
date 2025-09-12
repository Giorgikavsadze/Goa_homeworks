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