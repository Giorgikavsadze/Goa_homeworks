function discountFunc(){
    let User=Number(prompt("Enter your age: "))

    if (User<18){
        console.log("discount is 20%")

    }

    else if (User>=18 && User<65){
        console.log("discount is 5%")
    }
    else{
        console.log("discount is 10%")
    }

}