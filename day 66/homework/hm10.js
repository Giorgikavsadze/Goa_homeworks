function alertValue(e){

    e.preventDefault()

    let form = document.getElementById("main-form")
    let value = form.elements.phone.value
    alert(value)
    

    form.reset()
}