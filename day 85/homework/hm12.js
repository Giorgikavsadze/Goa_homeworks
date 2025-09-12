function outer() {
    let value = 5;
    console.log(value)

    function inner() {
        value = 10
    }

    inner()

    console.log(value)
}

outer();