// Extract Names from Objects
// Given [{name: "Alice"}, {name: "Bob"}], print each name.
const arr = [
    {name: "Alice"},
     {name: "Bob"}
];

arr.forEach(obj => {
    console.log(obj.name);
});