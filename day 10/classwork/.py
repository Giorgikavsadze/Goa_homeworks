
#შექმენით 3 ცვლადი, თითოეულში შეინახეთ მომხმარებლის შემოტანილი რიცხვი (გამოიყენეთ int ან float), შემდეგ დაბეჭდეთ ეს სამივე ცვლადი

num1=int(input("enter number1: "))
num2=float(input("enter number2: "))
num3=int(input("enter number3: "))

print(num1)
print(num2)
print(num3)


#საკლასო დავალება: შექმენით BMI კალკულატორი.
# მომხმარებელს უნდა შეეკითხოთ წონა და სიმაღლე, შეინახეთ ათწილადის სახით.
# შემდეგ შექმენით bmi ცვლადი, რომელიც ტოლია წონა / სიმაღლე ** 2. 
# საბოლოოდ დაბეჭდეთთ ამ ცვლადის მნიშვნელობა


weight=float(input("enter your weight: "))
height=float(input("enter your height: "))

bmi = (weight/height**2)

print(bmi)

#გააკეთეთ 5 მაგალითი თითო შედარების ოპერატორზე (>, <, >=, <=, ==, !=.)

print(7>3)
print(4>5)
print(6>7)
print(10>5)
print(9>4)

print(3<7)
print(3<6)
print(7<9)
print(1<6)
print(4<8)

print(7<=7)
print(5<=6)
print(1<=7)
print(8<=2)
print(2<=6)

print(10 >= 5)
print(4>=8)
print(6>=8)
print(4>=8)
print(1>=6)

print(3==8)
print(2==6)
print(7==9)
print(5==7)
print(3==6)

print(1!=9)
print(4!=8)
print(1!=4)
print(9!=6)
print(7!=0)