function CheckIfPosOrNeg(){

    let num = Number(prompt("Enter Number"))

    if (num > 0){
        console.log("Number is Positive")
    }

    else if(num< 0){
        console.log("Number is Negative")
    }

    else{
        console.log("Number equals to zero")
    }

}


CheckIfPosOrNeg()