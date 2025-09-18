// Falsy Value Detection
// Determine if any element is falsy (0, false, null, undefined, "", NaN).


const arr = [0, false, null, undefined, "", NaN]
const hasFalsy = arr.some(el => !el)
console.log(hasFalsy)