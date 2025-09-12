let ul = document.createElement("ul")
document.body.appendChild(ul)

let count = 0

let interval = setInterval(function () {
    count++
    
    let li = document.createElement("li")
    li.textContent = "Message " + count
    ul.appendChild(li)

    if (count === 10) {
        clearInterval(interval)
    }
}, 2000)