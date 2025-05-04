# 2)მომხმარებელს შემოატანინეთ რაღაც მონაცემი (მაგ:სახელი ან გვარი) და try,except ბლოკების საშუალებით გააკონტროლეთ ყველა ერორის შემთხვევა რაც არსებობს


try:
    user = input("Enter your name or surname: ")

    number = int(user) 

    lst = [1, 2, 3]
    print(lst[5])  

    result = 10 / 0 

except ValueError:
    print("ValueError: მონაცემი ვერ გადაკეთდა რიცხვად")

except TypeError:
    print("TypeError: სხვადასხვა ტიპის მონაცემებს ვერ შეასრულებ ერთად")

except ZeroDivisionError:
    print("ZeroDivisionError: ნულზე გაყოფა შეუძლებელია")

except IndexError:
    print("IndexError: სიაში მითითებული ინდექსი არ არსებობს")

except NameError:
    print("NameError: ცვლადი არ არის განსაზღვრული")