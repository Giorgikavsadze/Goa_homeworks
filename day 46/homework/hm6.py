# 8) Create a list comprehension that extracts words with more than 4 letters from a given list of words.

words=["Goa" ,"pc", "Computer" ,"cases"]
list1= [i for i in words if len(i) > 4]
print(list1)