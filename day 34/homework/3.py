# 5) Default Arguments: Define a function that takes a name as input and prints a greeting. If no name is provided, it should use "Guest" as the default.





def greet():
    name = input("Enter your name: ") 

    if name == "":  
        name = "Guest"

    print(f"Welcome, {name}!")

greet()  



