let button=document.getElementById("button")
let image=document.getElementById("img")
button.addEventListener("click" ,function(){
    if (image.style.display == "none") {
        image.style.display = "block"
    } else {
        image.style.display = "none"
    }

})