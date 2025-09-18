// Extract Names
// From [{name: "Alice", age: 25}, {name: "Bob", age: 30}], return ["Alice", "Bob"].

let arr=[{name: "Alice", age: 25}, {name: "Bob", age: 30}]
const names = arr.map(obj => obj.name)

console.log(names)