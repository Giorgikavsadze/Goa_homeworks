#საკლასო დავალება: True, False ბულეანებზე ჩამოწერეთ 4 კომბინაცია.
# ეს გააკეთეთ ან ოპერატორზეც და და ოპერატორზეც.
# თითეოული კომბინაციის შედეგი უნდა დაიბეჭდოს და მარჯვნივ მიუწერეთ კომენტარის სახით შედეგი რაც არის

print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False

print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False


#მომხმარებელს ინფუთით შემოატანინეთ რიცხვი და გადააქციეთ ის მთელი რიცხვად, შეინახეთ ცვლადში. ასევე იგივე გააკეთეთ მეორე რიცხვზე.
#შემდეგ დაბეჭდეთ: პირველი რიცხვი მეტია 30-ზე და მეორე ნაკლებია 40-ზე

number=(int(input("Enter number: ")))
number1=(int(input("Enter number: ")))

print(number> 30)
print(number1 < 40)