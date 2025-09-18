// Write a function that ensures all email addresses in an array contain "@".
const EmailAddresses=EmailArr=>{
    return EmailArr.every(i=>i.includes("@"))



}
console.log(EmailAddresses(["sunny.day92@example.com","techguru45@mailbox.net","blue.sky.creative@domain.org","coffee.lover99@gmail.com","traveler123@yahoo.com"]))