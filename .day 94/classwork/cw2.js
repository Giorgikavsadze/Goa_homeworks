const check = punctuation=>{
    return punctuation.endsWith(".")|| punctuation.endsWith("?") || punctuation.endsWith("!")
}

console.log(check("FDAFDAFDA!"))
console.log(check("FDAFDAFDA"))
console.log(check("FDAFDAFDA?"))
console.log(check("FDAFDAFDA."))
console.log(check("FDAFDAFDA"))
