# Use filter() to keep strings longer than 5 characters from a list of strings.


longer_5=list(filter(lambda name : len(name) > 5, ["Ioane","Giorgi","Beqa","data","Nikolozi"]))
print(longer_5)