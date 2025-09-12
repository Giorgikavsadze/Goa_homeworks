const arr=["Apple","banana",10,21,true,false]

for(let i of arr){
    if(typeof i ==="string"){
        console.log(i)
    }
    else if(typeof i==="number"){
        console.log(i+10)
    }
    else if(typeof i==="boolean"){
        console.log(!i)
    }
}