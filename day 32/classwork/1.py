# საკლასო დავალება:

# თქვენს ფუნქციაში format ფუნქციის მაგივრად გამოიყენეთ f string


def generate_big_sentence(name,surname,age):
    print(f"My name is {name},my surname is {surname},my age is {age}.")


name=input("Enter your name: ")
surname=input("Enter your surname: ")
age=input("Enter your age: ")

generate_big_sentence(name,surname,age)