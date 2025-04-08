# საკლასო დავალება:

# შექმენით ფუნქცია სახელად manual_list, რომელსაც ექნება 4 პარამეტრი: start, end, step, user_num.

# თქვენი დავალებაა, რომ ფუნქციამ დააბრუნოს სია, რომელშიც იქნება რიცხვები არჩეული (start, end, step) დიაპაზონის მიხედვით, უბრალოდ ეს რიცხვები მეტი უნდა იყოს user_num.

# ფუნქცია გამოიძახეთ 3-ჯერ, განსხვავებული არგუმენტებით

def manual_list(start, end, step, user_num):
    return [i for i in range(start, end, step) if i > user_num]

print(manual_list(10, 50, 5, 20))
print(manual_list(0, 30, 3, 10))    
print(manual_list(100, 200, 20, 150))
