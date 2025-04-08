#საკლასო დავალება: მომხმარებელს შემოატანინეთ რიცხვი და შეინახეთ ის ცვლადში მთელი რიცხვის სახით.
# შემდეგ შექმენით დიაპაზონი 0-დან ამ რიცხვამდე და დაბეჭდეთ დიაპაზონის ყველა რიცხვის ჯამი.
# გამოიყენეთ for ციკლი

num=int(input("Enter number: "))
sum=0
for i in range(num):
    sum = sum + i
    print(sum)



#საკლასო დავალება: 
# შექმენით correct_password ცვლადი და მასში შეინახეთ ნებისმიერი სთრინგი.
# სანამ მომხმარებლის შემოტანილი პაროლი არ იქნება correct_password-ის ტოლი, თავიდან შეეკითხეთ.
# საბოლოოდ, დაუბეჭდეთ access granted და ასევე რამდენჯერ მოუწია პაროლის შემოტანა.
# დაგჭირდებათ while loop, counter variable


correct_password = "12345678"
user_guess = input("Enter password: ")
counter = 0

while user_guess != correct_password:
    user_guess = input("Enter password: ")
    counter += 1

print("Access granted")
print("Your guess count:", str(counter))


# საკლასო დავალება:

# რიცხვის გამოცნობის პროგრამა:

# შექმენით my_num ცვლადი და 1-დან 10-მდე ნებისმიერი რიცხვი მიანიჭეთ მნიშვნელობად.

# სანამ მომხმარებლის შემოტანილი რიცხვი არ იქნება my_num-ის ტოლი, ისევ შეეკითხეთ მომხმარებელს ეს რიცხვი.

# საბოლოოდ დაუბეჭდეთ "you guessed" და რამდენი ცდა დაჭირდა

my_num=4
user = int(input("Enter number: "))
counter = 0

while user != my_num:
    user = int(input("Enter number: "))
    counter += 1

print("correct")
print("Your guess count:", str(counter))


