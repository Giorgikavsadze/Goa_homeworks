let count = 0

let interval = setInterval(function () {
    if (count % 2 === 0) {
        document.title = "Hello"
    } else {
        document.title = "Goodbye"
    }

    count++

    if (count >= 6) {
        clearInterval(interval)
    }
}, 1000)