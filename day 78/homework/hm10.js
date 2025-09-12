let div = document.getElementById("div")
let pos = 0

setInterval(function() {
    pos += 5
    div.style.left = pos + "px"
}, 100)