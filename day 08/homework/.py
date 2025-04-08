#4)მომხმარებელს შემოატანინეთ სახელი და გვარი, შეინახეთ ისინი ცვლადებში. შემდეგ დაუბეჭდეთ: "გამარჯობა {სახელი აქ} {გვარი აქ}."

name=input("enter your name: ")
surname=input("enter your surname: ")
age=input("enter your age: ")

print(name)
print(surname)
print(age)

#5) შექმენით 5 ცვლადი და მათში შეინახეთ რიცხვები. შემდეგი 6 ოპერატორის გამოყენებით: +, -, *, /, **, %  ჩამოწერეთ მათ შორის მათემატიკური ოპერაციები. ჩამოწერეთ ასეთი 10 მაგალითი.
#მაგალითად: print((num1 + num2) / num3 - num4*num5 + num1**num3 % num2)

num=5
num1=6
num2=10
num3=4
num4=2

print((num + num1) / num2 - num3 * num4 + num3**num2 % num2)
print(num+num1%num2*num3/num4-num2**num2)
print(num4*num/num1**num2+num3-num2%num3)
print(num2-num1+num/num3%num4**num*num1)
print(num1+num2-num3/num4*num%num2**num)
print(num/num1%num2*num3**num4-num+num2)
print(num*num1/num2%num4-num3+num4**num3)
print(num1+num2-num3/num4*num**num4%num3)
print(num/num2*num3-num4+num**num2%num2)
print(num4*num-num2+num3/num4%num**num2)
print(num1/num2-num3+num4**num%num2*num3)