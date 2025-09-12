const Double = arr => {
    let NewArr = [];
    for (let i of arr) {
        NewArr.push(i * 2)
    }
    console.log(NewArr)
};

Double([1, 2, 3, 4, 5])