#13) Write a function that takes a list, an index, and an item, and inserts the item at the specified index.


def insert_at_index(alist, index, item):
    alist.insert(index, item)
    print(alist)

insert_at_index(["apple", "orange", "banana"],1,"kiwi")