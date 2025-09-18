// საკლასო დავალება:შექმენით ინტერვალი,რომელიც 1 წუთის განმავლობაში, ტერმინალში ყოველ წამს გამოიტანს ახლანდელ დროს შემდეგ ფორმატში:
//  "წელი-თვე-დღე, საათი-წუთი-წამი"
let counter =0
const myinterval = setInterval(() => {
    const now = new Date()

    const year = now.getFullYear()
    const month = now.getMonth() + 1
    const day = now.getDate()

    const hour = now.getHours()
    const minute = now.getMinutes()
    const second = now.getSeconds()

    

    console.log(`${year}-${month}-${day}, ${hour}-${minute}-${second}`)
    if(counter===60){
        clearInterval(myinterval)
    }
}, 1000)
