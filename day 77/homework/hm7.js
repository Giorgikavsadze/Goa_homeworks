let numbers = [10, 20, 30, 40]
let sum = numbers.reduce(function(total, num) {
    return total + num
}, 0)

let average = sum / numbers.length;

console.log("Average:", average);