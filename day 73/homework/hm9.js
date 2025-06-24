let body=document.getElementById("body")
let ul=document.createElement("ul")
let li=document.createElement("li")
li.textContent="tomato"
let li1=document.createElement("li")
li1.textContent="apple"
body.appendChild(ul)
ul.appendChild(li)

ul.replaceChild(li1,li)
