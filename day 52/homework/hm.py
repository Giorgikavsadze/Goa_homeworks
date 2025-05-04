#2) პირველი ამოცანა:

#Find the first non-consecutive number

def first_non_consecutive(arr):
    if len(arr) < 2:
        return "Array is too short"
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    
    return None




