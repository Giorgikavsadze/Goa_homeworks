# საკლასო დავალება:

# შექმენით ფუნქცია სახელად generate_big_sentence, რომელსაც გადაეცემა 3 პარამეტრი - name, surname, age.

# ფუნქციამ უნდა გამოგვიტანოს წინადადება ზუსტად იგივე წყობით, როგორც მე დავწერე (გადახედეთ რესურებს), გამოიყენეთ format ფუნქცია.

# სანამ ფუნქციას გამოიძახებთ, მომხმარებელს შემოატანინეთ ტერმინალიდან სახელი, გვარი, ასაკი და შეინახეთ ისინი ცვლადებში.

# ფუნქციის გამოძახებისას, მას არგუმენტებად უნდა გადაეცეს ეს ცვლადები



def generate_big_sentence(name,surname,age):
    print("My name is {},my surname is {},my age is {}.".format(name,surname,age))


name=input("Enter your name: ")
surname=input("Enter your surname: ")
age=input("Enter your age: ")

generate_big_sentence(name,surname,age)