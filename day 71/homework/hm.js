let randomNum = Math.round(Math.random() * 100)
while (true) {
    let userNum = Number(prompt("შეიყვანეთ სასურველი რიცხვი"))

    if (userNum > randomNum) {
        alert("მეტია")
    } else if (userNum < randomNum) {
        alert("ნაკლებია")
    } else {
        alert("ტოლია")
        break
    }
}