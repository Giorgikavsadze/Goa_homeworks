function clearValue(e){

    e.preventDefault()

    let form = document.getElementById("main-form")
    let value = form.elements.email.value

    form.reset()
}