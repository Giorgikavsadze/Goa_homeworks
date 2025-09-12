

const words=arr=>{
    let letters=0
    for(let i of arr){
        if(i.length<1){
            continue
        }
        else if(i[0] === "A" || i[0] === "a"){
            letters++

        }
        
    }
    console.log(letters)
}