const oddNums=arr=>{
    for(let i of arr){
        if(i%2===0){
            continue
        }
        console.log(i)
    }
}

oddNums([1,2,3,4,5,6,7,8,9,10])