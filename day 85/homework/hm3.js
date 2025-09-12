function func(a,b,c,d){
    for(let i of arguments){
        if(i===0){
            break
        }
        console.log(i)
    }
    
}

func(10,20,0,40)