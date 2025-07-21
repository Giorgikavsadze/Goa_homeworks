let divs=document.getElementsByClassName("divs")

for(let i=0;i<divs.length;i++){
    divs[i].style.backgroundColor="black"
    divs[i].style.width="200px"
    divs[i].style.height="200px"
    divs[i].style.borderRadius="20px"
    divs[i].style.position="relative"

    let pos=0

    setInterval(function(){
        pos+=10
        divs[i].style.left=pos + "px"
    },1000)
    

}