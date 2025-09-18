// საკლასო დავალება:Given an array of objects with status property, verify that all items have status: "active".

const arr1=[
    {
        status:"active"
    },
    {
        status:"active"
    },
    {
        status:"active"
    },
    {
        status:"active"
    },
    {
        status:"active"
    }
]

console.log(arr1.every(object =>object.status==="active"))