let NewArr=[]
const arr=arr=>{
    for(let i of arr){
        if(NewArr.length>=5){
            break
        }
        if(i%2===1){
            continue
        }

        NewArr.push(i)
        

        
    }
    console.log(NewArr)
}
arr([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])