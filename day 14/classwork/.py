#for ციკლის გამოყენებით 20-ჯერ დაბეჭდეთ თქვენი სახელი და გვარი

for i in range(20):
    print("Giorgi Kavsadze")


#საკლასო დავალება:
# მომხმარებელს შემოატანინეთ რიცხვი და შეინახეთ მთელი რიცხვის სახით. იგივე გაიმეორეთ მემეორე ცვლადზე.
# for ციკლით იტერაცია მოახდინეთ დიაპაზონზე, რომლის საწყისი რიცხვია პირველი ცვლადი და საბოლოო რიცხვია მეორე ცვლადი.
# ციკლის ყოველ იტერაციაზე დაბეჭდეთ საიტერაციო ცვლადის კვადრატი

number, number1=int(input("Enter number: ")), int(input("Enter number: "))


for i in range(number,number1):
    print(i**2)
    


#ციკლის იტერაციაზე იბეჭდება:
# საიტერაციო ცვლადის კვადრატი,
# სტ. ცვლადი + პირველი რიცხვი,
# სტ. ცვლადი + მეორე რიცხვი,
# სტ. ცვლადი * პირველი რიცხვი,
# სტ. ცვლადი * მეორე რიცხვი






#Task: Print the Squares of Numbers
# Write a Python program that:
# Asks the user to enter a number 
# 𝑛
# n.
# Uses a for loop to print the square of each number from 1 to 
# 𝑛
# n.


n = int(input("Enter number: "))

for i in range(n) :
    print(i**2)




