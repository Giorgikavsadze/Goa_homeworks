#4) დაბეჭდეთ "GOA BEST!!!" 50-ჯერ, ორივე ციკლით შეასრულეთ ეს დავალება


for i in range(50):
    print("GOA BEST!!!")

GOA_BEST=50
while GOA_BEST > 0:
    print("GOA BEST!!!")
    GOA_BEST= GOA_BEST-1


# 5) Write a program that uses a while loop to count from 1 to 10 and prints each number.

loop = 1
while loop < 11 :
    print(loop)
    loop= loop + 1

#6) Use a while loop to print all even numbers between 1 and 20.

loop=2
while loop <21:
    print(loop)
    loop=loop+2

#7) Create a countdown from 10 to 1 using a while loop, and print "Blast off!" when the countdown finishes.

loop=10
while loop > 0:
    print(loop)
    loop= loop - 1
print("Blast off!")

#8) Prompt the user to enter a password. Keep asking until they enter the correct password.

password=5921
user=int(input("Enter password: "))
counter= 0
while user !=password: 
    user = int(input("Enter password: "))
    
    counter += 1
print("correct!!!")
print("number of your guesses:", str(counter))


#9) Create a program that keeps asking for a username and password until both are correct.

Username="Giorgi"
User=input("Enter your username: ")

counter=0

while User != Username :
    User=input("Enter your username: ")
    counter += 1

print("correct!!!")
print("number of your guesses:", str(counter))

Password=23
User1=int(input("Enter your password: "))
counter=0

while User1 != Password:
    User1=int(input("Enter your password: "))
    counter += 1

print("correct!!!")
print("number of your guesses:", str(counter))





