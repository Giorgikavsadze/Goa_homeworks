let box = document.getElementById("main_div")
box.style.width = "200px"
box.style.height = "200px"
box.style.backgroundColor = "black"
box.style.position = "relative"


let count = 0

let interval = setInterval(function () {
    if (count >= 100) {
        clearInterval(interval)  
    } else {
        box.style.left = count + "px"
        count+=10
    }
}, 200)