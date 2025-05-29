#You're a square!  
def is_square(n):    
    if n < 0:
        return False
    x = int(n ** 0.5)
    return x * x == n


#Get the Middle Character
def get_middle(s):
    length = len(s)
    if length % 2 == 0:
        return s[length // 2 - 1 : length // 2 + 1]
    else:
        return s[length // 2]
    

#Isograms
def is_isogram(string):
    string = string.lower()
    return len(set(string)) == len(string)

#Exes and Ohs

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


#Jaden Casing Strings   
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())