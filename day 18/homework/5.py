#8) Create a while loop that asks the user to enter a password. Keep asking until they enter the correct password "Goa best". Also print the count of incorrect passwords.



User=input("Enter password: ")

correct_password="Goa best"

while User!=correct_password:
    print("uncorrect!!!")
    User=input("Enter password: ")
print("correct!!!")