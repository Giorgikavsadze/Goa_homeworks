count=1
let interval=setInterval(function(){
    let randomNumber = Math.floor(Math.random() * 10) + 1
    console.log(randomNumber)
    count++
    if (count>5){
        clearInterval(interval)
    }
},1500)