// Check whether a user input string is empty after trimming (i.e., contains only spaces).
const user=prompt("Enter String")
trimed=user.trim()
if(trimed===""){
    console.log( "This string is empty")
}
else{
    console.log("this string contains something")
}