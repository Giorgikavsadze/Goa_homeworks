#12) Create a function that appends all elements of one list to another list.

def function(list1, list2):
    for i in list2:
        list1.append(i)

    print(list1)

function(["orange", "7", "8", "9"],["apple", "1", "2", "3"])