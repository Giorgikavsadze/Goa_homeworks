GuessNum=Math.round(Math.random()*100)
console.log(GuessNum)

User=Number(prompt("Guess number from 1 to 100"))

if (User===GuessNum){
    console.log("this is the correct number")
}
else if(User>GuessNum){
    console.log("Guessed number is more than the random number")
}
else if(User<GuessNum){
    console.log("Guessed number is less than the random number")
}
else{
    console.log("...")
}