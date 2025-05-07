# Use filter() to keep names that start with the letter 'A' from a list of names.

name_A=list(filter(lambda name:name[0]=="A",["Ioane","Andria","Beqa","Aleqsandre","Nikolozi"]))
print(name_A)