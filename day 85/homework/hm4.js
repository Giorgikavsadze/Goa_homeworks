function func(a,b,c,d,e){
    for(let i of arguments){
        if(typeof i==="string"){
            continue
        }
        console.log(i)
    }


}

func(1,2,"Hello",4)