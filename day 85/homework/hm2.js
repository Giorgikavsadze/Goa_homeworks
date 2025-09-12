function sum(a, b, c) {
    let total = 0
    for (let i of arguments) {
        total += i
        
    }
    console.log(total)
}

sum(10, 20, 30)