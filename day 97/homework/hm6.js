// Create a function that checks if a filename starts with "img_" and returns "Image file" or "Not an image file".
const NameOfTheFile=filename=>{
    const check=filename.startsWith("img_")
    if(check){
        return "Image file"
    }
    else{
        return "Not an image file"
    }

}

console.log(NameOfTheFile("img_of_the_pc"))

