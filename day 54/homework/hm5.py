# Return a Function – Multiplier
# Create a function that returns another function which multiplies any number by a given factor.

def function(factor):
    def multiplier(number):
        return number * factor
    return multiplier


three = function(3) 


result =three(10)  

print(result) 