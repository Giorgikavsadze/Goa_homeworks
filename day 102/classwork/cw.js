// საკლასო დავალება:html-ის დოკუმენტში ჩაამატეთ ერთი პარაგრაფი და ერთი ღილაკი.
// ორივე ელემენტი წამოიღეთ js-ში. შემდეგ, შექმენით მასივი, სადაც გექნებათ 5 სთრინგი. როდესაც მომხმარებელი დააკლიკებს ღილაკს, 
// თქვენ მასივიდან ერთ-ერთი random სთრინგი უნდა აირჩიოთ (გამოიყენეთ Math.random მეთოდი) და ეს სთრინგი textContent-ად გაუწეროთ პარაგრაფს.

const btn=document.getElementById("btn")
const para=document.getElementById("para")

const myArr=["apple","computer","goa","mobile","fork"]

btn.addEventListener("click", ()=>{
    const randomIndex = Math.floor(Math.random() * myArr.length)
    para.textContent = myArr[randomIndex]

    

})

