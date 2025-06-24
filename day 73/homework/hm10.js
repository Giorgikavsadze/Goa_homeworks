let header=document.getElementById("header")
let header1=document.createElement("h1")
header1.textContent="Hello,How are you?"

let body=document.getElementById("body")

body.replaceChild(header1,header)