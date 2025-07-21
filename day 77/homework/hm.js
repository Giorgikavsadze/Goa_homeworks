let count = 10

let countdown = setInterval(function() {
    console.log(count)
    count--

    if (count < 0) {
        clearInterval(countdown)
        console.log("Time's up!")
    }
}, 1000)