let image=document.getElementsByTagName("img")
for(let i=0;i<image.length;i++){
    image[i].style.width="200px"
    image[i].style.borderRadius="10px"
    if (image[i].alt.includes("cat")) {
        image[i].style.border = "2px solid orange"
    }
}