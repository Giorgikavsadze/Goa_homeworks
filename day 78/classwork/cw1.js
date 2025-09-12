let div = document.getElementById("div");

for(let i = 0; i < 5; i++) {
    let p = document.createElement("p");
    p.textContent = "paragraph N" + (i + 1);
    div.appendChild(p);
}