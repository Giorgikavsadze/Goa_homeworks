#4) Write a program that takes a score (0-100) as input and outputs the grade based on the following rules:

# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F


grade=int(input("Enter your grade: "))

if 90 <= grade <= 100:
    print("A")
elif 80 <= grade <= 89:
    print("B")
elif 70 <= grade <= 79:
    print("C")
elif 60 <= grade <= 69:
    print("D")
elif 0<= grade < 60 :
    print("F")
else:
    print("incorrect grade")




