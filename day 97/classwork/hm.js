// საკლასო დავალება:Create a function that takes a sentence string and returns the total number of words.
//  Make sure to remove extra spaces at the beginning, end, and between words before counting.

const NumOfWords=(sentence)=>sentence.trim().split(" ").length


console.log(NumOfWords("        Hello world                   "))