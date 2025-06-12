function changeElements(){
    let Header=document.getElementById("header")
    let Button=document.getElementById("button")
    let input=document.getElementById("text")

    
    console.log(input.value)

    Button.style.backgroundColor="black"
    Button.style.color="white"
    Header.style.textAlign="center"
    document.body.style.backgroundColor="green"
    
}

changeElements()