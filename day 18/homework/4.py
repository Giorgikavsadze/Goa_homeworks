#7) Ask the user to enter a number multiple times and check if it's even or odd. Stop after 5 numbers.


for User in range(5):
    User=int(input("enter number: "))


if User%2 == 0:
    print("even")
else:
    print("odd")