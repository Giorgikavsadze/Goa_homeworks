// On form submit, log the value of the input with name="username" to the console.

function FormSubmit(e){
    e.preventDefault()

    let form = document.getElementById("main-form")
    let value= form.elements.username.value
    console.log(value)

    form.reset()

}