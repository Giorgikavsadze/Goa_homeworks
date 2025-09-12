const sumNums = arr => {
    let sum = 0
    for (let i of arr) {
        if (i <= 0 || i % 2 !== 0) {
            continue
        }
        sum += i
    }
    console.log(sum)
};

sumNums([2, -4, 5, 8, -10, 3, 12])