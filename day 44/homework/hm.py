# 2) პირველი დავალების ამოცანებიდან აირჩიეთ ნებისმიერი და დეტალურად გაარჩიეთ მისი კოდი კომენტარების სახით

#DNA to RNA Conversion
def dna_to_rna(dna):
    return dna.replace("T","U")

print(dna_to_rna("GCAT"))

#ამ ფუნქციაში return-ს გადაეცემა replace მეთოდი რომელიც მოქმედებს dna პარამეტრზე. replace-ით ჩვენ სიტყვა GCAT-ის T ასო უნდა შევცვალოთ U-თი და გამოვა GCAU