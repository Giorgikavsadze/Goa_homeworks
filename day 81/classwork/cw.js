let sum=0

do {
    let User=Number(prompt("Enter num: "))
    sum += User
    let li=document.createElement("li")
    li.textContent=sum
    document.body.appendChild(li)
} while(sum <=100)