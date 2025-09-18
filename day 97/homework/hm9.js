// Create a function that counts how many names in an array start with "Dr.".
const NameCount=Myarr=>{
    count=0
    for(let i of Myarr){
        if(i.startsWith("Dr.")){
            count++
        }
    }
        return count
}

console.log(NameCount(["Dr.Alonso","Max","Dr.lewis","Checo","isack"]))