let count = 0

let interval = setInterval(function () {
    console.log("Hello My name is Giorgi")
    count++

    if (count === 5) { 
        clearInterval(interval)
    }
}, 2000)