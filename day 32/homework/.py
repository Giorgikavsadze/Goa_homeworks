# 3) Write a function that takes a user's name and age, and returns a welcome message formatted with an f-string.


User=input("Enter your name: ")
User1=input("Enter your age: ")

def name_age(string,string1):
    print(f"welcome! {User},your age is {User1}.  ")

name_age(User,User1)
