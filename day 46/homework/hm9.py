# 11) Create a list comprehension that extracts all words from a given sentence that contain at least one vowel and are longer than 5 characters.

sentence = ["Goal-oriented-academy is the best "] 
words = sentence[0].split()  

list1 = [i for i in words if len(i) > 5 and ('a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i)]

print(list1)