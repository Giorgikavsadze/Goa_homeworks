const numCheck=()=>{
    const func=i=>{
        if(isNaN(i)){
            console.log("Not a number")
        }
        else{
            console.log("number")
        }
        


        

    }

    const user=prompt("enter value")
    const user1=prompt("enter value")
    
    func(user)
    func(user1)


}

numCheck()