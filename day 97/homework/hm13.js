// Write a function that takes a list of usernames (with random spaces around them) and returns clean usernames without leading or trailing spaces.
const ListOfUsernames=Usernames=>{
    NewArr=[]
    for(let i of Usernames){
        NewArr.push(i.trim())
    }
    console.log(NewArr)


}

ListOfUsernames(["    Giorgi   ","   Nika","daviti          ","   saba     ","     ioane     "])