# Use filter() to remove empty strings from a list of strings.

empty=list(filter(lambda string:string!="",["","Giorgi","Beqa","data",""]))
print(empty)