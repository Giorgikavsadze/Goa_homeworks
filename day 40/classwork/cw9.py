#10) Convert number to reversed array of digits
def digitize(n):
    starting_str = str(n)
    reversed_str = starting_str[::-1]

    res_list = []

    for i in reversed_str:
        res_list.append(int(i))

    return res_list

# ამ ფუნქციაში ჩვენ უნდა დავაბრუნოთ ლისტის სახით მოცემული ლისტი ოღონდ შემოტრიალებულად აქ ჯერ ვაქცევთ სტრინგათ შემდეგ კი ვატრიალებთ და შემდეგ უკვე 
#ახალ ლისტში უნდა მოვათავსოთ შემოტრიალებული ციფრები.