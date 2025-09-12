let div=document.createElement("div")
let div1=document.createElement("div")
let div2=document.createElement("div")
div.className="circle"
div1.className="circle"
div2.className="circle"
document.body.appendChild(div)
document.body.appendChild(div1)
document.body.appendChild(div2)
let divs=document.getElementsByClassName("circle")
for(let i=0;i<divs.length;i++){
    divs[i].style.width="50px"
    divs[i].style.height="50px"
    divs[i].style.borderRadius="50%"
    divs[i].style.backgroundColor="purple"
    divs[i].style.marginTop="20px"
    divs[i].style.position="relative"
    let pos=0
    let interval=setInterval(function(){
    pos =pos+10
    divs[i].style.left=pos + "px"

    


    },200)
}



