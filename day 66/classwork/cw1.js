function GetFormData(e){
    e.preventDefault()

    let form=document.getElementById("main-form")
    let input= form.elements.name.value
    alert(input)

    form.reset()
}