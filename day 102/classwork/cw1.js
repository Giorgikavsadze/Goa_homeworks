// საკლასო დავალება:html-ის დოკუმენტში ჩაამატეთ პარაგრაფი და ღილაკი. 
// როდესაც მომხარებელი დააკლიკებს ღილაკს, პარაგრაფის textContent უნდა გახდეს დღევანდელი დღე - ამისთვის გამოიყენეთ Date ობიექტი, getDay მეთოდი და მასივი.

const p=document.getElementById("para")
const btn=document.getElementById("button")
const myArr=["sunday","Monday","Tuesday","wednesday","Thursday","friday","saturday"]

btn.addEventListener("click",()=>{
    const today=myArr[new Date().getDay()]
    
    p.textContent=today

})