function Combine(e){
    e.preventDefault()
    let name = document.getElementById("name").value
    let surname = document.getElementById("surname").value
    let header = document.getElementById("header")

    let combined=name+ " " + surname

    header.textContent=combined

    
}