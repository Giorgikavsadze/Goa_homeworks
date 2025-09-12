{
    let a=10
    console.log(a)
}
console.log(a) //error-ია რადგან როდესაც ცვლადი შექმნილია let keyword-ით ბლოკის გარეთ ვერ მიწვდები ცვლადს block scope-ის გამო.

{
    const b=20
    console.log(b)
}
console.log(b) //error-ია რადგან როდესაც ცვლადი შექმნილია const keyword-ით ბლოკის გარეთ ვერ მიწვდები ცვლადს block scope-ის გამო.

{
    var c=30
    console.log(c)
}
console.log(c) //error-აღარ იქნება რადგან var keyword-ის გამოყენების დროს შენ შეგიძლია ბლოკიდან ცვლადის წამოღება
// უპრობლემოდ block scope-ის უქონლობის გამო რაც მოუხერხებელს ხდის var-ს.


