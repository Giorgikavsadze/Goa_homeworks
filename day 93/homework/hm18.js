const user=prompt("enter your weight: ")
const user1=prompt("enter your height in meters: ")

const weight=parseFloat(user)
const height=parseFloat(user1)
const bmi=weight/(height**2)
console.log(bmi)