let listItems = document.getElementsByTagName("li");

for (let i = 0; i < listItems.length; i++) {
if (listItems[i].textContent.length > 10) {
    listItems[i].style.backgroundColor = "lightpink";
} else {
    listItems[i].style.backgroundColor = "lightgreen";
}
}