let interval =setInterval(function(){
    console.log("გიორგი კავსაძე")
},10000)

let button= document.getElementById("button")

button.addEventListener("click",function(){
    clearInterval(interval)
})
