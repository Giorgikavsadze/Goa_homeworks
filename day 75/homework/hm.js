let count = 1

let interval = setInterval(function() {
    console.log(count)
    count++

    if (count > 5) {
        clearInterval(interval)
    }
}, 1000)