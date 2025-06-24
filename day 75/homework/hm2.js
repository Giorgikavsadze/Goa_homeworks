let count=0
let arr=["black","purple","blue","yellow","green"]

function ChangeBc(){
    document.body.style.backgroundColor=arr[count]
    count++
    if(count===5){
    clearInterval(interval)
}
}

interval=setInterval(ChangeBc,3000)

