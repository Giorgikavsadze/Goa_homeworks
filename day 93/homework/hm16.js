const billAmount=prompt("Enter Bill Amount: ")
const tipPercentage=prompt("Enter tip percentage: ")

const bill=parseFloat(billAmount)
const tip=parseFloat(tipPercentage)
const tipAmount = bill * (tip / 100)
const wholeAmount=bill+tipAmount

console.log(wholeAmount)