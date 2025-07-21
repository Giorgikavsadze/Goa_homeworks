let arr=[1,2,3,4,5,6]
let interva=setInterval(function(){
    for (i=0;i<arr.length;i++){
        console.log(i)
    }
},1000)

let arr1=[7,8,9,10,11]
for(i=0;i<arr1.length;i++){
    arr[i]=arr1[i]
}
