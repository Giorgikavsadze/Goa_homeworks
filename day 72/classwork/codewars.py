# Shortest Word
def find_short(s):
    words = s.split()                      
    lengths = [len(i) for i in words] 
    shortest = min(lengths)                
    return shortest 


#String ends with?

def solution(text, ending):
    return text.endswith(ending)

#Mumbling

def accum(st):
    result = []
    for i in range(len(st)):
        c = st[i]
        result.append(c.upper() + c.lower() * i)
    return '-'.join(result)


#Sum of two lowest positive integers


def sum_two_smallest_numbers(numbers):
    sort=sorted(numbers)
    return sort[0]+sort[1]

#Complementary DNA

def DNA_strand(dna):
    dna = dna.replace('A', 'X')
    dna = dna.replace('T', 'A')
    dna = dna.replace('X', 'T')

    dna = dna.replace('C', 'Y')
    dna = dna.replace('G', 'C')
    dna = dna.replace('Y', 'G')

    return dna


#Beginner Series #3 Sum of Numbers

def get_sum(a, b):
    start = min(a, b)
    end = max(a, b)
    return sum(range(start, end + 1))


#Friend or Foe?
def friend(x):
    return [i for i in x if len(i) == 4]

#Credit Card Mask

def maskify(cc):
    if len(cc) <= 4:
        return cc
    return '#' * (len(cc) - 4) + cc[-4:]

#Binary Addition
def add_binary(a, b):
    return bin(a + b)[2:]