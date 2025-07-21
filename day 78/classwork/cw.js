let p=document.getElementsByTagName("p")
let texts=[]
for(let i=0;i<p.length;i++){
    texts[i]=p[i].textContent

}

console.log(texts)
