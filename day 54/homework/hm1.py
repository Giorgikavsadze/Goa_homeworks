# List Index Access
# Create a small list and ask the user for an index to access. Handle the case when the index is out of range.


list1=['cat',152,14,"Goa"]
User=int(input("Enter index: "))
try:
    
    print(list1[User])
except IndexError:
    print("your index is out of range")

