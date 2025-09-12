let my_ObJ = {
    name: "Giorgi",
    surname: "Kavsadze",
    academy: "Goal-oriented-academy"
}

let key = "name"

for (let i in my_ObJ) {
    if (i === key) {
        console.log("Key exists!");
        break;
    }
    else{
        console.log("key does not exists!")
    }
}