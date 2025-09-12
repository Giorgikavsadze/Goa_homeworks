let btn = document.getElementById("button");
    let div = document.getElementById("div");

    div.style.width = "200px";
    div.style.height = "200px";
    div.style.backgroundColor = "black";
    div.style.position = "relative";


    let colors = ["red", "blue", "green", "orange", "purple"];
    let pos = 0;
    let clicks = 0;
    let maxClicks = 10;

    btn.onclick = function () {
    if (clicks < maxClicks) {
        let rand = Math.floor(Math.random() * colors.length);
        div.style.backgroundColor = colors[rand];

        pos += 10;
        div.style.left = pos + "px";

        clicks++;
    }
    };