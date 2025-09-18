// Prime Number Detection
// Check if any number in an array is prime.

const arr = [10, 20, 30, 40, 5, 7, 17]

function isPrime(num) {
  if (num < 2) return false
  for (let i = 2; i < num; i++) { 
    if (num % i === 0) return false
  }
  return true
}

const hasPrime = arr.some(isPrime)

console.log(hasPrime)