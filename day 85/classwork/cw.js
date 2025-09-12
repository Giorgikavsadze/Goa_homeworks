function tenPara(a,b,c,d,e,f,g,h,i,j){
    for(let i of arguments){
        if(i%2===0){
            console.log(i)
        }
    }
}
tenPara(1,2,3,4,5,6,7,8,9,10)