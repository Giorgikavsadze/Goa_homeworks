#4) შექმენით დიაპაზონი 20-დან 50-მდე და შეინახეთ ცვლადში

num=20
num1=50
for i in range(num,num1):
    print(i)


#5) შექმენით დიაპაზონი 100-დან 150-მდე და შეინახეთ ცვლადში

num=100
num1=150
for i in range(num,num1):
    print(i)

#6) შექმენით 20-დან 50-მდე ლუწი რიცხვების დიაპაზონი და შეინახეთ ცვლადში

num=20
num1=50
num2=2
for i in range(num,num1,num2):
    print(i)

#7) შექმენით 11-დან 31-მდე კენტი რიცხვების დიაპაზონი და შეინახეთ ცვლადში

num=11
num1=31
num2=2
for i in range(num,num1,num2):
    print(i)

#8) for ციკლით 10-ჯერ დაბეჭდეთ თქვენი სახელი და გვარი

for i in range(20):
    print("Giorgi kavsadze")

#9) 10-დან 30-მდე დაბეჭდეთ ყველა რიცხვი გაყოფილი 2-ზე

num=10
num1=31
for i in range (num,num1):
    print(i/2)

#10) 40-დან 60-მდე დაბეჭდეთ ყველა რიცხვის მესამე ხარისხი

num=40
num1=61
for i in range (num,num1):
    print(i**3)

#11) 5-ჯერ შეეკითხეთ მომხმარებელს რიცხვი და ხუთივეჯერ დაბეჭდეთ. შეასრულეთ ციკლით, პირდაპირ დაწერილი არ ითვლება


for i in range(5):
    num=int(input("Enter number: "))
    print(num)

#12) მომხმარებელს შეეკითხეთ სახელი და მოახდინეთ მასზე იტერაცია for ციკლით, დაბეჭდეთ სახელის თითოეული ასო

name=(input("Enter your name: "))
for i in name:
    print(i)

#13) მომხმარებელს შეეკითხეთ რიცხვი და შეინახეთ num1 ცვლადში მთელი რიცხვის სახით.
# მომხმარებელს შეეკითხეთ რიცხვი და შეინახეთ num2 ცვლადში მთელი რიცხვის სახით.
# მომხმარებელს შეეკითხეთ რიცხვი და შეინახეთ num3 ცვლადში მთელი რიცხვის სახით.
# შექმენით შემდეგი დიაპაზონი: range(num1, num2, num3)
# გადაუარეთ ამ დიაპაზონს for ციკლით და დაბეჭდეთ საიტერაციო ცვლადის კვადრატები

num1,num2,num3=int(input("Enter number: ")),int(input("Enter number: ")),int(input("Enter number: "))
range= range(num1, num2, num3)
for i in range:
    print(i**2)

#14) ციკლის გარეთ შექმენით ცვლადი სახელად sum და გაუტოლეთ 0-ს. 
#ციკლით იტერაცია მოახდინეთ 5-დან 15-ის ჩათვლით და თითოეული საიტერაციო ცვლადი დაუმატეთ num ცვლადს. საბოლოოდ დაბეჭდეთ sum ცვლადის მნიშვნელობა

sum = 0 
for i in range(5,16):
    print(sum + i)






