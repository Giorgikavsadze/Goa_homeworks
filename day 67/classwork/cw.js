let object={

    name:"Giorgi",
    surname:"Kavsadze",
    academy:"Goal-oriented-academy",
    city:"tbilisi",
    role:"student",
    favColor:"Green",

    nameSurname(){
        console.log(this.name + " " + this.surname)

    },

    favcolor(){
        console.log(this.favColor)
    }


}


console.log(object)
console.log(object.city)
object.nameSurname()
object.favColor="Blue"
console.log(object.favColor)

