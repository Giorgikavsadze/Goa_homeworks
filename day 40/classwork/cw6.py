# #7) Basic Mathematical Operations
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif  operator == "-":
        return value1 - value2
    elif  operator == "*":
        return value1 * value2
    elif  operator == "/":
        return value1 / value2
    else:
        return ("incorrect operator")
    
# ამ ფუნქციაში გვაქვს კალკულატორის მსგავსი ფუნქცია რომელიც მაშინ იმოქმედებს თუ ოპერატორი + ტოლი იქნება და იგი დააბრუნებს პარამეტრების value1 და value2-ის მიმატებას 
#დანარჩენს ოპერატორებზეც იგივე პრინციპით რომლებიცაა: მინუსი,გამრავლება და გაყოფა.