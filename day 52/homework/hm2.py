#4) 3 ამოცანა 
#Correct the mistakes of the character recognition software
def correct(s):
    s = s.replace("5", "S")
    s = s.replace("0", "O")
    s = s.replace("1", "I")
    return s