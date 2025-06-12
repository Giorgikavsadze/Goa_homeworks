let User = Number(prompt("Enter number: "))

if (User%3==0 && User%5==0){
    console.log("Divisible by both")
}
else if (User%3==0){
    console.log("Divisible by 3")
}
else if (User%5==0){
    console.log("Divisible by 5")
}
else{
    console.log("not divisible by any")
}
