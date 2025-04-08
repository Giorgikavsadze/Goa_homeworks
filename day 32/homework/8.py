# 11) Create a function that takes a list and a list of items, and appends each item to the original list.

def lists(alist,list_of_items):
    for item in list_of_items:
        alist.append(item)
    print(alist)

lists(["apple", "1", "2", "3"],["orange", "7", "8", "9"])