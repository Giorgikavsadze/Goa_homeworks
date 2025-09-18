// Sum of Numbers
// Calculate and print the sum of all numbers in an array.

const arr = [1,2,3,4,5,6,7,8,9,10];
let total = 0;

arr.forEach(num => {
    total += num
})

console.log(total)