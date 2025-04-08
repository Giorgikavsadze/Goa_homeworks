# შექმენით ფუნქცია სახელად remove_one_element, რომელსაც გადაეცემა სია და ინდექსი.

# სიიდან მაგ ინდექსზე მყოფი ელემენტი ამოშალეთ და დაბეჭდეთ სია.

def remove_one_element(lists,ind):
    lists.pop(ind)
    print(lists)

list=[1,23,4,5,45,1,13,12]
indx=4

remove_one_element(list,indx)