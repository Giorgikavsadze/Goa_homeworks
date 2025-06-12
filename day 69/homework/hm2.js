let User = Number(prompt("Enter number: "))
let User1 = Number(prompt("Enter number: "))
let User2 = Number(prompt("Enter number: "))

if (User > User1 && User > User2) {
    console.log(User)
}
else if (User1 > User && User1 > User2) {
    console.log(User1)
}
else if (User2 > User && User2 > User1) {
    console.log(User2)
}
else {
    console.log("Numbers are equal")
}