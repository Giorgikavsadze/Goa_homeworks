count=0

function simpleTimer(){
    count++
    console.log(count)

    if(count===10){
        clearInterval(interval)
    }
}

interval=setInterval(simpleTimer,1000)

