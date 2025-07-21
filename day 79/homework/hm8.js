let div=document.getElementById("div")
let btn=document.getElementById("btn")
div.style.height="200px"
div.style.width="200px"
div.style.backgroundColor="black"
btn.addEventListener("click", function () {
    div.style.display = "none"

    
    let interval = setInterval(function () {
        div.style.display = "block"
        clearInterval(interval)
    }, 5000)
})
