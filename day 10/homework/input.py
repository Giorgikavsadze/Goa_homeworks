# 6) მომხმარებელს შემოატანინეთ ასაკი და დაუბეჭდეთ 10 წელში რამდენი წლის იქნება

age = int(input("Enter your age: "))
future_age = age + 10
print(future_age)


# 7) სამ ადამიანს შემოატანინეთ ასაკები და გამოითვალეთ ამ ასაკების საშუალო არითმეტიკული (ასაკების ჯამი / ადამიანების რაოდენობა)

age  =int(input("Enter your age: "))
age1 =int(input("Enter your age: "))
age2 =int(input("Enter your age: "))

arithmetic_mean = (age + age1 + age2) / 3
print(arithmetic_mean)

# 8) მომხმარებელს შემოატანინეთ 2 რიცხვი და დაბეჭდეთ ამ რიცხვების: ჯამი, სხვაობა, ნამრავლი, განაყოფი, პირველი რიცხვი ხარისხად მეორეზე, მეორე რიცხვი ხარისხად პირველზე

num =int(input("Enter number: "))
num1=int(input("Enter number: "))

total = num + num1
difference = num - num1
division = num/num1
exponentiation = num**num1
exponentiation1 = num1**num

print(total)
print(difference)
print(division)
print(exponentiation)
print(exponentiation1)

# 9) მომხმარებელს შემოატანინეთ 3 რიცხვი და დაბეჭდეთ ამ რიცხვების: ჯამი, სხვაობა, ნამრავლი, განაყოფი


num = int(input("Enter number: "))
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))

total = num + num1 + num2
difference = num - num1 - num2
product = num * num1 * num2
division = num / num1 / num2

print(total)
print(difference)
print(product)
print(division)
