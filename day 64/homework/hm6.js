function ChangeColor(e){
    e.preventDefault()
    let body = document.getElementById("body")
    let color = document.getElementById("input1").value
    

    body.style.backgroundColor = color
}