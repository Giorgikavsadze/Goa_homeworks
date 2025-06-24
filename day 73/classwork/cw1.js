function changeElements(){
    
    let div=document.getElementById("main-div")
    let button = document.getElementById("button")
    let paragraph=document.getElementById("para")

    div.removeChild(button)

    let i = document.createElement("i")
    i.textContent = "hello"

    div.replaceChild(i,paragraph)
}

changeElements()