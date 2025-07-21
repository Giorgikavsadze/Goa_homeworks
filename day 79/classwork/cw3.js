let div = document.createElement("div");
let btn = document.createElement("button");
btn.textContent = "Click Me";
div.style.width = "300px";
div.style.height = "300px";
div.style.backgroundColor = "purple";
div.style.marginBottom = "10px";
document.body.appendChild(div);
document.body.appendChild(btn);
let counter = 1;
let interval;
btn.addEventListener("click", function () {
    if (interval) clearInterval(interval);
    let size = 300;
    div.style.display = "block";
    interval = setInterval(function () {
        let p = document.createElement("p");
        let text = document.createTextNode("p" + counter);
        p.appendChild(text);
        document.body.appendChild(p);
        counter++;
        size -= 20;
        if (size <= 0) {
            div.style.display = "none";
            clearInterval(interval);
        } else {
            div.style.width = size + "px";
            div.style.height = size + "px";
            div.style.backgroundColor = getRandomColor();
        }
    }, 3000);
});
function getRandomColor() {
    let letters = "0123456789ABCDEF";
    let color = "#";
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}