// Create a function that checks if every student in an array of objects has passed (score >= 50).

const arr=[
    {
        studentScore:50
    },
    {
        studentScore:20
    },
    {
        studentScore:49
    },
    {
        studentScore:67
    },
    {
        studentScore:100
    }
]

console.log(arr.every(object=>object.studentScore>=50))