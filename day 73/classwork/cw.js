function addNewElement(){
    let div=document.getElementById("main-div")
       

    let button=document.createElement("button")
    button.textContent="Click me"

    div.appendChild(button)
}

addNewElement()