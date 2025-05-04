#6) 5 ამოცანა 
#Do I get a bonus?

def bonus_time(salary, bonus):
    if bonus == True:
        return "$" + str(salary * 10)
    elif bonus == False:
        return "$" + str(salary)