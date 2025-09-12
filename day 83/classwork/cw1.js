const arr=arr=>{
    for(let i of arr){
        if(i.length<=5){
            continue
        }
        console.log(i)
    }
}
arr(["apple","banana","Goa","Monitor","hello","ram","bmw","audi","computer","watch"])