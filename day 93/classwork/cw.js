

const NumCheck=()=>{
    const func = i =>{
        if(isNaN(i)){
            console.log("Is not a number")
        }
        else{
            console.log("is a number")
        }
    }

    const value=prompt("Enter value")
    const value1=prompt("Enter value")

    func(value)
    func(value1)

}

NumCheck()