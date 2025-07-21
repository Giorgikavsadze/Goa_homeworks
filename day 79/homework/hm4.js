let lis=document.getElementsByTagName("li")
for (let i = 0; i < lis.length; i++) {
    if (i % 2 === 0) {
        lis[i].style.backgroundColor = "skyblue"
    } else {
        lis[i].style.backgroundColor = "lightgray"
    }
}