let favMovies=["iron man","fast and the furious 1","fast and the furious 2","real steel","fast and the furious 3"]

let User=prompt("Guess my favourite movies: ")

if (favMovies.includes(User)){
    console.log("Yes, it's one of my favorites!")
}
else{
    console.log("No, I don't like that one much.")
}