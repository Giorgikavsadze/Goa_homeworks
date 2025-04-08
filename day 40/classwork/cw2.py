#3) Remove String Spaces
def no_space(x):
    return x.replace(" ", "")

#აქ გვეუბნებიან რომ space უნდა ამოიშალოს.ამ ფუნქციაში ჩვენ replace-ის გამოყენებით x პარამეტრში " "(space-ს) ვცვლით ""(no space-ში) 
# ანუ space ები ამოიშლება რადგან მას ჩაანაცვლებს არა space("").