# 2)Create a list and try to access an index that does not exist. Handle IndexError.

try:
    list1=[1,2,3,4,5]
    print(list1[5])
except IndexError:
    print("list1-ში მეხუთე ინდექზე არაფერია")