let btn=document.createElement("button")
let div=document.createElement("div")
document.body.appendChild(btn)
document.body.appendChild(div)
div.style.width="200px"
div.style.height="200px"
div.style.position="relative"
div.style.backgroundColor="black"
btn.textContent="Click me"

const colors=["orange","green","blue"]


pos=0
addEventListener("click",function(){
    pos+=20
    div.style.left=pos + "px"
    
    let randomColor = colors[Math.floor(Math.random() * colors.length)];
    div.style.backgroundColor = randomColor;
})