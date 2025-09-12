
const sumOfPosNums=arr=>{
    let sum=0
    for (let i of arr) {
        if (i < 0) break
        sum += i
    }
    console.log(sum)
}

sumOfPosNums([5,6,-7,8])