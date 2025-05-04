# Function as Argument – Greeting
# Write a function that takes another function as an argument and calls it to print a greeting.


def function(greeting_func):
    greeting_func("Hello")

def greeting(message):
    print(message)


function(greeting)
        
