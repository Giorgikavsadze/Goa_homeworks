#4
#Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence
def replace_exclamation(st):
    vowels = "aeiouAEIOU"
    result = ""
    for i in st:
        if i in vowels:
            result += "!"
        else:
            result += i 
    return result