# Use map() to concatenate the string "Hello " to each name in a list of names.

list1=["Nika","Giorgi","Beqa","data","luka"]
hello=lambda name: "Hello" + " " + name
print(list(map(hello,list1)))