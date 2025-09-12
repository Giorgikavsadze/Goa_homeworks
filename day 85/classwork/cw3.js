// block scope
{
    let x=10
    console.log(x)
}
console.log(x)

// function scope
function func(){
    let y=20
    console.log(y)
}
console.log(y)


// global scope

let z=30
console.log(z)

{
    console.log(z)
}
