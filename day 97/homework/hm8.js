// Write a function that checks if a string starts with a specific substring at a given position.
const startsWithAt = (str, substring, position) => {
    return str.startsWith(substring, position);

}

console.log(startsWithAt("Hello world","Hello",0))