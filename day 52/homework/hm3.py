#5) 4 ამოცანა 
#Is it a palindrome?

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]