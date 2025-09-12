let sum=0
const arr=[1,21,5,10,13,5]
for(let i of arr){
    sum+=i
    if(sum>=50){
        break
    }
    
}
console.log(sum)