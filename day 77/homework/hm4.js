let arr = ["apple", "banana", "orange"]
let arr1 = ["bmw", "mercedes", "audi"]
let arr2 = ["cpu", "gpu", "ram"]

function logUppercase(array) {
    for (let i = 0; i < array.length; i++) {
        console.log(array[i].toUpperCase())
    }
}

logUppercase(arr)
logUppercase(arr1)
logUppercase(arr2)