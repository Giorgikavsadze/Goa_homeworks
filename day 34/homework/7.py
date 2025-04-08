# 9) Define a function that takes a list of integers and returns a new list containing only the positive numbers. Use a loop and a conditional statement.

def list_of_integers(int_list):
    new_list=[]
    for i in int_list:
        if i >0:
            new_list.append(i)

    print(new_list)


list_of_integers([-1,-3,2,-4,2,5,-6])
