# Use map() to convert a list of strings to uppercase.


list1=["Giorgi","Kavsadze","Goal","Oriented","Academy"]
upper_case=lambda string:string.upper()
print(list(map(upper_case,list1)))