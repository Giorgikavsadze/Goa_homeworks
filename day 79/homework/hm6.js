let inputs=document.getElementsByTagName("input")

for(let i=0;i<inputs.length;i++){
    inputs[i].addEventListener("input", function () {
        if (inputs[i].value.length > 20) {
            inputs[i].style.backgroundColor = "red"
        } else {
            inputs[i].style.backgroundColor = "white"
        }
    })
}


