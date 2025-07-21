# შეასრულეთ მსგავსი,უბრალოდ ჩაშენებული(sum) ფუნქციის გარეშე
def odd_or_even(arr):
    total = 0
    for i in arr:
        total += i 
        
    

    if total %2==0:
        return "even"
    else:
        return "odd"
    
print(odd_or_even([1,2,3,4,5,6]))