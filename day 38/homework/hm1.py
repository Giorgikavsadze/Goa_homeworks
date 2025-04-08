# 3) Tuple Immutability: Try to modify an element in a tuple and observe what happens.

tuple1=(1,2,3,4,5)
tuple1[1] = 10
print(tuple1[1])

#ამოაგდებს ერორს რადგან tuple-ში ელემენტების შეცვლა არ შეიძლება ანუ tuple უცვლელია.
