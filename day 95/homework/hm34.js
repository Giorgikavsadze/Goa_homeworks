// Write a function that returns the first half of any given string using slice.
function FirstHalf(string) {
  const half = Math.floor(string.length / 2)
  return string.slice(0, half)
}

console.log(FirstHalf("Banana"))
console.log(FirstHalf("computer"))
console.log(FirstHalf("paper"))