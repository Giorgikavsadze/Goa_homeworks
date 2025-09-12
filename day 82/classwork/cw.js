function sumNumbers(){
    let sum=0
    let i=0
    while(i<10){
        i++
    
    if(i%2===1){
        continue
    }
    sum+=i
}
    return sum
}

console.log(sumNumbers())