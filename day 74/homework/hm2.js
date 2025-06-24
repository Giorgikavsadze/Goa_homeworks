let div=document.getElementById("main-div")
div.style.width="200px"
div.style.height="200px"
div.style.backgroundColor="black"

div.addEventListener("click",function(){
    if (div.style.backgroundColor === "black") {
        div.style.backgroundColor = "green"
    } else {
        div.style.backgroundColor = "black"}
    

})