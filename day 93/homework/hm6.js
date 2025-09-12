const age =()=>{
    const User=prompt("Enter your age")
    if(isNaN(User)){
        console.log("invalid age")
    }
    else{
        console.log("valid age")
    }
}

age()