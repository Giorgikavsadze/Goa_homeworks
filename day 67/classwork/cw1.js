function userOperations(){
    let Positive = confirm("are you student?")
    let Negative = confirm("do you live in tbilisi")

    console.log(Positive && Negative)
    console.log(Positive || Negative)
}

userOperations()