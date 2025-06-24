let count = 0

let interval = setInterval(function () {
    count++
    console.log(count)

    if (count === 15) {
        clearInterval(interval)
    }
}, 1000)