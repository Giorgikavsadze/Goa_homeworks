const PosNums=arr=>{
    for(let i of arr){
        if(i<0){
            continue
        }
        console.log(i)
    }
}
PosNums([1,2,3,-4,-7,43,-91])