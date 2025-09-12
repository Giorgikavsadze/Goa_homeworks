let ul=document.getElementById("ul")
let myObj = {
    name: "David",
    surname: "Tezelashvili",
    academy: "GOA",
    isMentor: true,
    num: 100,
    hobbies: ["programming", "bike", "basketball"],
    favColor: "Blue"
}

for(let key in myObj){
    let li=document.createElement("li")
    let li1=document.createElement("li")
    let hr=document.createElement("hr")
    li.textContent=key
    li1.textContent=myObj[key]

    ul.appendChild(li)
    ul.appendChild(li1)
    ul.appendChild(hr)

}