# საკლასო დავალება:

# შექმენით ფუნქცია სახელად no_duplicates, რომელსაც გადაეცემა ერთი პარამეტრი - user_list.

# user_list-ის მონაცემთა ტიპია სია, ხოლო თქვენი დავალებაა რომ ფუნქციამ დააბრუნოს ეს სია იმ სახით, რომ მასში დუპლიკატები არ გვქონდეს. 

# ფუნქცია გამოიძახეთ 3-ჯერ, განსხვავებული არგუმენტებით

def no_duplicates(user_list):
    no_duplicates_list=list(set(user_list))
    return no_duplicates_list


print(no_duplicates([1,1,2,2,3,3,4,4]))
print(no_duplicates(["a","b","b","a"]))
print(no_duplicates([5,5,5,6,6,6,7,7,7]))