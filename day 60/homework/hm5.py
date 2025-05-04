#6
#Add Length
def add_length(s):
    words = s.split()  
    result = []
    for i in words:
        result.append(f"{i} {len(i)}") 
    return result
        