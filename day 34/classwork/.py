# საკლასო დავალება:

# შექმენით ფუნქცია რომელიც მიიღებს ორ პარამეტრს - main_list, indexes_list.

# თქვენი დავალებაა, რომ indexes_list სიაში რა ინდექსებიც იქნება მოცემული, მთავარ სიაში, მაგ ინდექსებზე წაშალოთ ელემენტები


def function( main_list, indexes_list):
    for i in indexes_list:
        main_list.pop(i)

    print( main_list)



function([1,2,3,4,5,6,7,8],[5,3])
