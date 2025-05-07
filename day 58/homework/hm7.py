# Use map() to find the length of each word in a list of strings.

list1=["Giorgi","Kavsadze","Goal","Oriented","Academy"]
length=lambda string:len(string)
print(list(map(length,list1)))